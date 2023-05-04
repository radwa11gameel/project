from rest_framework import serializers
from .models import Doctor, Patient, MedicalRecord,Prediction,Classification
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):
  class Meta:
        model = Prediction
        fields = '__all__' 

class ClassificationSerializer(serializers.ModelSerializer):
  class Meta:
        model = Classification
        fields = '__all__' 


