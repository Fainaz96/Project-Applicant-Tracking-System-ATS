import google.generativeai as genai
from django.conf import settings
import json
import os

# Configure GenAI
if settings.GOOGLE_API_KEY:
    genai.configure(api_key=settings.GOOGLE_API_KEY)

class BaseAgent:
    def __init__(self, model_name="gemini-2.5-flash"):
        self.primary_model_name = model_name
        self.fallback_model_name = "gemini-2.5-flash"
        self.model = genai.GenerativeModel(self.primary_model_name)
        self.fallback_model = genai.GenerativeModel(self.fallback_model_name)

    def generate(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e) or "Quota exceeded" in str(e):
                print(f"Warning: Quota exceeded for {self.primary_model_name}. Retrying with fallback {self.fallback_model_name}...")
                try:
                    response = self.fallback_model.generate_content(prompt)
                    return response.text
                except Exception as e2:
                    print(f"Error generating content with fallback: {e2}")
            else:
                print(f"Error generating content: {e}")
            return None

class ParsingAgent(BaseAgent):
    def parse_resume(self, resume_text):
        prompt = f"""
        You are an expert Resume Parsing Agent. Extract the following information from the resume text provided below.
        Return ONLY a valid JSON object. Do not include any markdown formatting (like ```json).
        
        Fields to extract:
        - name (string)
        - email (string)
        - phone (string)
        - experience_summary (string, max 100 words summary)
        - skills_raw (list of strings)
        - education (list of objects with degree, institution, year)
        
        Resume Text:
        {resume_text}
        """
        response_text = self.generate(prompt)
        if response_text:
            clean_text = response_text.replace("```json", "").replace("```", "").strip()
            try:
                return json.loads(clean_text)
            except json.JSONDecodeError:
                print("Failed to decode JSON from Parsing Agent")
                return None
        return None

class SkillExtractionAgent(BaseAgent):
    def extract_skills(self, resume_text):
        prompt = f"""
        You are a Skill Extraction Agent. Analyze the resume text and identify technical and soft skills.
        Return ONLY a valid JSON object.
        
        Output format:
        {{
            "tech_skills": ["skill1", "skill2"],
            "soft_skills": ["skill1", "skill2"],
            "confidence_score": 0.0 to 1.0 (float reflecting overall confidence in extraction)
        }}
        
        Resume Text:
        {resume_text}
        """
        response_text = self.generate(prompt)
        if response_text:
            clean_text = response_text.replace("```json", "").replace("```", "").strip()
            try:
                return json.loads(clean_text)
            except json.JSONDecodeError:
                return None
        return None

class RankingAgent(BaseAgent):
    def rank_candidate(self, resume_text, job_description=""):
        context = f"Job Description: {job_description}" if job_description else "General Software Engineering Role"
        
        prompt = f"""
        You are a Ranking Agent. Evaluate the candidate based on the resume text against the context.
        Provide a scoring from 0 to 100 for Total Score, Skill Score, and Experience Score.
        Provide a brief reason (2 sentences).
        
        Context: {context}
        
        Resume Text (truncated):
        {resume_text[:4000]}
        
        Return ONLY valid JSON:
        {{
            "total_score": int,
            "skill_score": int,
            "experience_score": int,
            "reason": "string"
        }}
        """
        response_text = self.generate(prompt)
        if response_text:
            clean_text = response_text.replace("```json", "").replace("```", "").strip()
            try:
                return json.loads(clean_text)
            except json.JSONDecodeError:
                return None
        return None

class Orchestrator:
    def __init__(self):
        self.parser = ParsingAgent()
        self.extractor = SkillExtractionAgent()
        self.ranker = RankingAgent()

    def process_resume(self, resume_text, job_description=""):
        # 1. Parse
        parsed_data = self.parser.parse_resume(resume_text)
        
        # 2. Extract Skills
        skills_data = self.extractor.extract_skills(resume_text)
        
        # 3. Rank
        ranking_data = self.ranker.rank_candidate(resume_text, job_description)
        
        return {
            "parsed": parsed_data,
            "skills": skills_data,
            "ranking": ranking_data
        }
