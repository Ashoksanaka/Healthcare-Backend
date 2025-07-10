from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Patient

class TestPatient(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='patientuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_patient(self):
        url = reverse('patient-list')
        data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male',
            'address': '123 Main St',
            'phone': '1234567890',
            'email': 'johndoe@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_patients(self):
        Patient.objects.create(user=self.user, name='John Doe', age=30, gender='Male', address='123 Main St', phone='1234567890', email='johndoe@example.com')
        url = reverse('patient-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
