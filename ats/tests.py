from django.test import TestCase, Client
from django.urls import reverse
from .models import Job

class CareerPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.job = Job.objects.create(
            title="Test Job",
            description="Test Description"
        )

    def test_career_page_loads(self):
        """Test that the career page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Job")
