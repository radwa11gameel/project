from django.urls import path
from . import views,api
from .api import (
    DoctorListAPI, DoctorDetailAPI,
    PatientListAPI, PatientDetailAPI,
    MedicalRecordListAPI, MedicalRecordDetailAPI, PredictionAPI, PredictionListAPI,
    ClassificationAPI,ClassificationListAPI
)

app_name = 'myapp'


'''
    
    
http://127.0.0.1:8000/api/v1/
    
    
    
'''

urlpatterns = [
    # # URLs for doctors
    # path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    # path('doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor_detail'),
    # path('doctors/new/', views.DoctorCreate.as_view(), name='doctor_new'),
    # path('doctors/<int:pk>/edit/', views.DoctorUpdate.as_view(), name='doctor_edit'),
    # path('doctors/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor_delete'),

    # # URLs for patients
    
    # path('patients/', views.PatientList.as_view(), name='patient_list'),
    # path('patients/<int:pk>/', views.PatientDetail.as_view(), name='patient_detail'),
    # path('patients/new/', views.PatientCreate.as_view(), name='patient_new'),
    # path('patients/<int:pk>/edit/', views.PatientUpdate.as_view(), name='patient_edit'),
    # path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),
    # path('api/patient/<int:id>/', Classification.as_view(), name='patient_detail'),
    
    # # URLs for medical records
    # path('records/new/<int:patient_pk>/', views.MedicalRecordCreate.as_view(), name='medical_record_new'),
    # path('records/<int:pk>/edit/', views.MedicalRecordUpdate.as_view(), name='medical_record_edit'),
    # path('records/<int:pk>/delete/', views.MedicalRecordDelete.as_view(), name='medical_record_delete'),


    # API
    path('doctors/', DoctorListAPI.as_view(), name='doctor-list-api'),
    path('doctors/<int:pk>/', DoctorDetailAPI.as_view(), name='doctor-detail-api'),
    path('doctors/<int:pk>/edit/',DoctorDetailAPI.as_view(), name='doctor_edit-api'),
    path('doctors/<int:pk>/delete/',DoctorDetailAPI.as_view(), name='doctor_delete-api'),
    path('patients/', PatientListAPI.as_view(), name='patient-list-api'),
    path('patients/<int:pk>/', PatientDetailAPI.as_view(), name='patient-detail-api'),
    path('patients/<int:pk>/edit/', PatientDetailAPI.as_view(), name='patient_edit-api'),
    path('patients/<int:pk>/delete/',PatientDetailAPI.as_view(), name='patient_delete-api'),
    path('medical-records/', MedicalRecordListAPI.as_view(), name='medical-record-list-api'),
    path('medical-records/<int:pk>/', MedicalRecordDetailAPI.as_view(), name='medical-record-detail-api'),
    path('prediction/<int:id>/', PredictionAPI.as_view()),
    path('prediction/', PredictionAPI.as_view()),
    path('prediction/list/', PredictionListAPI.as_view()),
    path('classification/<int:id>/', ClassificationAPI.as_view()),
    path('classification/', ClassificationListAPI.as_view()),
    path('search/',api.search_models),




    
]





