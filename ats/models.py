from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, related_name='applicants')
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    experience_summary = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    parsed_data = models.JSONField(null=True, blank=True) # Full structured JSON from Parse Agent
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name or self.email or "Unknown Applicant"

class ApplicantSkill(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    confidence = models.FloatField(default=0.0)
    
    class Meta:
        unique_together = ('applicant', 'skill')

class Evaluation(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='evaluation')
    total_score = models.IntegerField(default=0)
    skill_score = models.IntegerField(default=0)
    experience_score = models.IntegerField(default=0)
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Score: {self.total_score} for {self.applicant}"
