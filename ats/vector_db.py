import google.generativeai as genai
from django.conf import settings
import os
import json
import math

# Configure GenAI
if settings.GOOGLE_API_KEY:
    genai.configure(api_key=settings.GOOGLE_API_KEY)

class VectorDB:
    def __init__(self):
        # Lightweight JSON storage
        self.file_path = os.path.join(settings.BASE_DIR, 'vectors.json')
        self.vectors = self._load_vectors()

    def _load_vectors(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def _save_vectors(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.vectors, f)

    def _get_embedding(self, text):
        try:
            # Use Gemini for embeddings (lightweight client)
            result = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document",
                title="Resume Embedding"
            )
            return result['embedding']
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []

    def _cosine_similarity(self, v1, v2):
        if not v1 or not v2: return 0.0
        dot_product = sum(a*b for a, b in zip(v1, v2))
        magnitude1 = math.sqrt(sum(a*a for a in v1))
        magnitude2 = math.sqrt(sum(b*b for b in v2))
        if magnitude1 == 0 or magnitude2 == 0: return 0.0
        return dot_product / (magnitude1 * magnitude2)

    def add_applicant(self, applicant_id, text_content, metadata=None):
        """
        Add applicant text to vector store.
        """
        if metadata is None: metadata = {}
        str_id = str(applicant_id)
        
        embedding = self._get_embedding(text_content)
        if embedding:
            self.vectors[str_id] = {
                "embedding": embedding,
                "metadata": metadata,
                "text": text_content[:200] # Store snippet only
            }
            self._save_vectors()

    def query_similar_applicants(self, query_text, n_results=5):
        """
        Find applicants similar to the query text.
        """
        query_embedding = self._get_embedding(query_text)
        if not query_embedding: return []

        scores = []
        for aid, data in self.vectors.items():
            score = self._cosine_similarity(query_embedding, data['embedding'])
            scores.append({
                'id': aid,
                'score': score,
                'metadata': data['metadata']
            })
        
        # Sort by score desc
        scores.sort(key=lambda x: x['score'], reverse=True)
        return scores[:n_results]

    def delete_applicant(self, applicant_id):
        str_id = str(applicant_id)
        if str_id in self.vectors:
            del self.vectors[str_id]
            self._save_vectors()
