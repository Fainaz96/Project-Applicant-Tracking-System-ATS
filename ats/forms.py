from django import forms
from .models import Applicant

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['resume']
