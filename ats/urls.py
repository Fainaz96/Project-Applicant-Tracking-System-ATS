from django.urls import path
from . import views

urlpatterns = [
    path('', views.career, name='career'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('apply/<int:job_id>/', views.upload_resume, name='apply_job'),
    path('applicant/<int:pk>/', views.applicant_detail, name='applicant_detail'),
]
