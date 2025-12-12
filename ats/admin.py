from django.contrib import admin
from .models import Applicant, Skill, ApplicantSkill, Evaluation, Job

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'total_score', 'skill_score', 'experience_score')
