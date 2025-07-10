from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor

class TestDoctor(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='doctoruser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_doctor(self):
        url = reverse('doctor-list')
        data = {
            'name': 'Dr. Smith',
            'specialization': 'Cardiology',
            'phone': '1234567890',
            'email': 'drsmith@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_doctors(self):
        Doctor.objects.create(user=self.user, name='Dr. Smith', specialization='Cardiology', phone='1234567890', email='drsmith@example.com')
        url = reverse('doctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
