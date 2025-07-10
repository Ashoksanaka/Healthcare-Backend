from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'age', 'gender', 'address', 'phone', 'email']
        read_only_fields = ['id', 'user']
