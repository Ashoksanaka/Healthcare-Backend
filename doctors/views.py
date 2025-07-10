from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all doctors
        return Doctor.objects.all()

    def perform_create(self, serializer):
        # Save the doctor with the current authenticated user
        serializer.save(user=self.request.user)
