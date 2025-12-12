import os
import django

# Manually load .env
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.partition('=')
                if key and value:
                    os.environ[key.strip()] = value.strip()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from ats.models import Job

# Create AI Engineer Job if not exists
if not Job.objects.filter(title="AI Engineer").exists():
    Job.objects.create(
        title="AI Engineer",
        description="""We are looking for an AI Engineer with experience in Python, Machine Learning, and LLMs.
        
        Responsibilities:
        - Design and build AI agents using Gemini.
        - Implement vector search using ChromaDB.
        - Integrate LLMs into Django web applications.
        
        Requirements:
        - 3+ years of Python experience.
        - Experience with LangChain or Google GenAI.
        - Familiarity with Vector Databases (ChromaDB, Pinecone)."""
    )
    print("Created 'AI Engineer' Job.")
else:
    print("'AI Engineer' Job already exists.")
