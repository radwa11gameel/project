from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, default='male')
    # classification = models.CharField(max_length=50, blank=True)
    # prediction = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name
    patientclassification=models.BooleanField(blank=True,default=False,null=True)
    patientprediction=models.BooleanField(blank=True,default=False,null=True)



class MedicalRecord(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    prescription = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.date}"


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile', unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, default='male')
    profile_photo = models.ImageField(blank=True, null=True)

    # specialty = models.CharField(max_length=255)
    # medical_license_number = models.CharField(max_length=255)
    # patients = models.ManyToManyField(Patient, related_name='doctors')

    def __str__(self):
        return f"{self.user}"



class Classification(models.Model):
    isexist=models.BooleanField(blank=True,default=False,null=True)
    patient = models.ForeignKey(Patient, verbose_name=("Patient"), on_delete=models.CASCADE)
    medicalphoto = models.ImageField(("Medical Photo"),upload_to='patient/images/')
    result = models.CharField(("Result"), max_length=50)
    def __str__(self):
        return f"{self.patient} - {self.result}"
    


class Prediction(models.Model):
    isexist=models.BooleanField(blank=True,default=False,null=True)
    patient = models.ForeignKey(Patient ,verbose_name=("Patient"),on_delete=models.CASCADE ) 
    medicalfile = models.FileField(("Medical File"), upload_to="patient/files/")
    result = models.CharField(("Result"), max_length=50)

    def __str__(self):
        return f"{self.patient} - {self.result}"


'''
classification.patient.gender
classification.patient.phone_number
'''


