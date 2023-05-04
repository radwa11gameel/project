from django.contrib import admin
from .models import Doctor, MedicalRecord, Patient,Prediction,Classification
# Register your models here.


admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(Patient)
admin.site.register(Prediction)
admin.site.register(Classification)