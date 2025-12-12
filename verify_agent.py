import os
import django
import json

# Manually load .env
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.partition('=')
                if key and value:
                    os.environ[key.strip()] = value.strip()

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from ats.agents import Orchestrator

def test_orchestrator():
    resume_text = """
    John Doe
    Email: john.doe@example.com
    Phone: 123-456-7890
    
    Summary:
    Experienced Software Engineer with 5 years in Python, machine learning, and web development.
    Passionate about building scalable AI systems.
    
    Skills:
    Python, Django, TensorFlow, Docker, AWS, Git, Communication, Leadership.
    
    Education:
    B.S. Computer Science, University of Tech, 2018.
    """
    
    print("--- Starting Orchestrator Test ---")
    orchestrator = Orchestrator()
    results = orchestrator.process_resume(resume_text, job_description="Looking for a Python backend engineer with ML experience.")
    
    print("\n--- Parsed Data ---")
    print(json.dumps(results['parsed'], indent=2))
    
    print("\n--- Extracted Skills ---")
    print(json.dumps(results['skills'], indent=2))
    
    print("\n--- Ranking ---")
    print(json.dumps(results['ranking'], indent=2))
    
    print("\n--- Test Complete ---")

if __name__ == "__main__":
    test_orchestrator()
