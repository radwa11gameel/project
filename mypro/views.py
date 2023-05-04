from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor, Patient, MedicalRecord

# def doctor_patients(request):
#     doctor_id = request.GET.get('doctor_id')
#     doctor = get_object_or_404(Doctor, id=doctor_id)
#     patients = doctor.patients.all()
#     medical_records = MedicalRecord.objects.filter(patient__in=patients)
#     context = {'doctor': doctor, 'patients': patients, 'medical_records': medical_records}
#     return render(request, 'doctor_patients.html', context)


class DoctorList(ListView):
    model = Doctor
    template_name = 'myapp/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'myapp/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'myapp/doctor_form.html'
    fields = ['user', 'age', 'address',
              'phone_number', 'gender', 'profile_photo']


class DoctorUpdate(UpdateView):
    model = Doctor
    template_name = 'myapp/doctor_form.html'
    fields = ['user', 'age', 'address',
              'phone_number', 'gender', 'profile_photo']


class DoctorDelete(DeleteView):
    model = Doctor
    template_name = 'myapp/doctor_confirm_delete.html'
    success_url = reverse_lazy('myapp:doctor_list')


class PatientList(ListView):
    model = Patient
    template_name = 'myapp/patient_list.html'
    context_object_name = 'patients'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'myapp/patient_detail.html'
    context_object_name = 'patient'


class PatientCreate(CreateView):
    model = Patient
    template_name = 'myapp/patient_form.html'
    fields = ['name', 'age', 'address', 'phone_number', 'gender',
              'medical_photo', 'classification', 'prediction']


class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'myapp/patient_form.html'
    fields = ['name', 'age', 'address', 'phone_number', 'gender',
              'medical_photo', 'classification', 'prediction']


class PatientDelete(DeleteView):
    model = Patient
    template_name = 'myapp/patient_confirm_delete.html'
    success_url = reverse_lazy('myapp:patient_list')


class MedicalRecordCreate(CreateView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_form.html'
    fields = ['patient', 'date', 'diagnosis', 'notes', 'prescription']

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.kwargs['patient_pk']
        return initial


class MedicalRecordUpdate(UpdateView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_form.html'
    fields = ['patient', 'date', 'diagnosis', 'notes', 'prescription']


class MedicalRecordDelete(DeleteView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('myapp:patient_detail', kwargs={'pk': self.object.patient.pk})


# login and logup
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
