import chromadb
from chromadb.utils import embedding_functions
from django.conf import settings
import os

class VectorDB:
    def __init__(self):
        # Persistent storage for ChromaDB
        persist_directory = os.path.join(settings.BASE_DIR, 'chroma_db')
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Use Google GenAI embeddings if key is present, otherwise valid default
        # Note: Chroma's default is Onnx/SentenceTransformers (local).
        # For simplicity and cost, we can use the default local embedding function for now,
        # or use Google's if we want to be fancy. The request says "Gemini Agent",
        # but embedding generator can be local model to save API calls, as per architecture diagram (Gemini / Local Model).
        # We'll use the default SentenceTransformer which is free and local.
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        
        self.collection = self.client.get_or_create_collection(
            name="applicant_embeddings",
            embedding_function=self.embedding_fn
        )

    def add_applicant(self, applicant_id, text_content, metadata=None):
        """
        Add applicant text to vector DB.
        """
        if metadata is None:
            metadata = {}
        
        # ID must be string
        str_id = str(applicant_id)
        
        self.collection.upsert(
            documents=[text_content],
            metadatas=[metadata],
            ids=[str_id]
        )

    def query_similar_applicants(self, query_text, n_results=5):
        """
        Find applicants similar to the query text (e.g. Job Description).
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def delete_applicant(self, applicant_id):
        self.collection.delete(ids=[str(applicant_id)])
