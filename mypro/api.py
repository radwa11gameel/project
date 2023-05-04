from rest_framework import generics
from rest_framework.views import APIView
from .models import Doctor, Patient, MedicalRecord, Prediction,Classification
from .serializers import DoctorSerializer, PatientSerializer, MedicalRecordSerializer,PredictionSerializer,ClassificationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .ml_prediction import * # to import file
# from .ml_prediction import predictions # for result
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .ml_prediction import *

class DoctorListAPI(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientListAPI(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MedicalRecordListAPI(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class ClassificationListAPI(generics.ListAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationAPI(APIView):
    
    def get(self, request, id):
        classification = Classification.objects.get(id=id)
        serializer = ClassificationSerializer(classification)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ClassificationSerializer(data=request.data)
        if serializer.is_valid():
            classification = serializer.save()
            classification.result = 'Positive'
            classification.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        classification = Classification.objects.get(id=id)
        serializer = ClassificationSerializer(classification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            classification = serializer.instance
            classification.result = 'Positive'
            classification.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class PredictionListAPI(generics.ListAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class PredictionAPI(APIView):

    def get(self, request, id):
        prediction = Prediction.objects.get(id=id)
        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)

    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():

            prediction = serializer.save()
            # prediction.result = 'Positive'
            prediction.save()
            
            # perform machine learning processing
            medicalfile = prediction.medicalfile.path
            df = pd.read_csv(medicalfile)
            df_processed = preprocessing_steps(df)
            predictions = extract_cat_num(df)
            # predictions = cat_col, num_col = extract_cat_num(df)
            cat_col, num_col = extract_cat_num(df)
            for col in cat_col:
                df[col] = le.fit_transform(df[col])
            selected_feat = ['donor_age', 'donor_age_below_35', 'donor_ABO', 'donor_CMV', 'recipient_age',
                            'recipient_gender', 'recipient_body_mass', 'recipient_ABO', 'recipient_rh',
                            'recipient_CMV', 'disease', 'disease_group', 'ABO_match', 'CMV_status',
                            'HLA_match', 'allel', 'HLA_group_1', 'risk_group', 'stem_cell_source',
                            
                            'tx_post_relapse', 'CD34_x1e6_per_kg', 'CD3_x1e8_per_kg',
                            'CD3_to_CD34_ratio', 'extensive_chronic_GvHD', 'relapse', 'survival_time']
            df = df[selected_feat]


            predictions = loaded_model.predict(df)

            prediction.result = predictions[0]
            # prediction.result = 'Positive'
            prediction.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        prediction = Prediction.objects.get(id=id)
        serializer = PredictionSerializer(prediction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            prediction = serializer.instance
            prediction.result = 'Positive'
            prediction.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def search_models(request):
    query = request.data.get('query', '')
    
    if query:

        prediction_result = Prediction.objects.filter(Q(patient__name__icontains=query))
        prediction_serializer = PredictionSerializer(prediction_result, many=True)


        classification_result = Classification.objects.filter(Q(patient__name__icontains=query))
        classification_serializer = ClassificationSerializer(classification_result, many=True)


        search_results = {
            'Prediction': prediction_serializer.data,
            'Classification': classification_serializer.data
        }
        return Response(search_results)
    
    else:
        return Response({'results': []})
