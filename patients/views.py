from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return patients created by the authenticated user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the patient with the current authenticated user
        serializer.save(user=self.request.user)
