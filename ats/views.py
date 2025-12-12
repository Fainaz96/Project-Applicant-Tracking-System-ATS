from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeUploadForm
from .models import Applicant, Evaluation, Skill, ApplicantSkill, Job

from .agents import Orchestrator
from .vector_db import VectorDB
from django.conf import settings
import os
try:
    import docx2txt
except ImportError:
    docx2txt = None
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == '.pdf':
        if PdfReader:
            try:
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            except Exception as e:
                print(f"Error reading PDF: {e}")
    elif ext == '.docx':
        if docx2txt:
            try:
                text = docx2txt.process(file_path)
            except Exception as e:
                print(f"Error reading DOCX: {e}")
    return text

def upload_resume(request, job_id=None):
    job = None
    if job_id:
        job = get_object_or_404(Job, pk=job_id)
        
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False) # Don't save yet
            if job:
                applicant.job = job
            applicant.save()
            
            # Processing Logic (Orchestrator)
            file_path = applicant.resume.path
            resume_text = extract_text_from_file(file_path)
            
            if resume_text:
                try:
                    orchestrator = Orchestrator()
                    # Pass Job Description context
                    jd_context = job.description if job else ""
                    results = orchestrator.process_resume(resume_text, job_description=jd_context)
                    
                    if not results or not results.get('parsed'):
                        raise ValueError("Failed to parse resume or AI quota exceeded.")

                    # Update Applicant
                    parsed = results['parsed']
                    email = parsed.get('email')
                    
                    if email:
                        # Handle Duplicate: Delete existing applicant with same email to replace with new one
                        # BUT, maybe we want to allow same person applying for different jobs?
                        # For now, let's keep it per-job unique or global unique. 
                        # To keep it simple, global unique overwrite for now as per previous logic.
                        existing = Applicant.objects.filter(email=email).exclude(pk=applicant.pk)
                        if existing.exists():
                           existing.delete()

                        applicant.email = email
                    
                    applicant.name = parsed.get('name')
                    applicant.phone = parsed.get('phone')
                    applicant.experience_summary = parsed.get('experience_summary')
                    applicant.parsed_data = parsed
                    applicant.save()
                    
                    # Save Skills
                    if results.get('skills'):
                        tech_skills = results['skills'].get('tech_skills', [])
                        confidence = results['skills'].get('confidence_score', 0.0)
                        for skill_name in tech_skills:
                            skill_obj, created = Skill.objects.get_or_create(name=skill_name.lower())
                            ApplicantSkill.objects.create(applicant=applicant, skill=skill_obj, confidence=confidence)
                    
                    # Save Evaluation
                    if results.get('ranking'):
                        Evaluation.objects.create(
                            applicant=applicant,
                            total_score=results['ranking'].get('total_score', 0),
                            skill_score=results['ranking'].get('skill_score', 0),
                            experience_score=results['ranking'].get('experience_score', 0),
                            reason=results['ranking'].get('reason', '')
                        )
                    
                    # Save to VectorDB
                    vdb = VectorDB()
                    vdb.add_applicant(applicant.id, resume_text, metadata={"name": applicant.name or "Unknown", "job": job.title if job else "General"})
                
                except Exception as e:
                    print(f"Error processing resume: {e}")
                    applicant.delete()
                    return render(request, 'ats/upload.html', {'form': form, 'error': f"Processing failed: {str(e)}", 'job': job})
                
            return redirect('dashboard')
    else:
        form = ResumeUploadForm()
    
    return render(request, 'ats/upload.html', {'form': form, 'job': job})

def career(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'ats/index.html', {'jobs': jobs})

def dashboard(request):
    applicants = Applicant.objects.all().order_by('-evaluation__total_score')
    return render(request, 'ats/dashboard.html', {'applicants': applicants})

def applicant_detail(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    return render(request, 'ats/detail.html', {'applicant': applicant})
