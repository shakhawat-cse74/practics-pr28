from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showdata(request):
    fm = StudentRegistration()
    return render (request,'enroll/registrationfrom.html', {'form':fm})