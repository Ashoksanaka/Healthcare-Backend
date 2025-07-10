from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from patients.models import Patient
from doctors.models import Doctor
from .models import PatientDoctorMapping

class TestMapping(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mappinguser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.patient = Patient.objects.create(user=self.user, name='John Doe', age=30, gender='Male', address='123 Main St', phone='1234567890', email='johndoe@example.com')
        self.doctor = Doctor.objects.create(user=self.user, name='Dr. Smith', specialization='Cardiology', phone='1234567890', email='drsmith@example.com')

    def test_create_mapping(self):
        url = reverse('mapping-list')
        data = {
            'patient': self.patient.id,
            'doctor': self.doctor.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_mappings(self):
        PatientDoctorMapping.objects.create(patient=self.patient, doctor=self.doctor)
        url = reverse('mapping-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_doctors_for_patient(self):
        PatientDoctorMapping.objects.create(patient=self.patient, doctor=self.doctor)
        url = reverse('mapping-doctors-for-patient', args=[self.patient.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_delete_mapping(self):
        mapping = PatientDoctorMapping.objects.create(patient=self.patient, doctor=self.doctor)
        url = reverse('mapping-detail', args=[mapping.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
