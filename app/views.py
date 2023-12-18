from django.shortcuts import render
from app.models import *
# Create your views here.
def dept(request):
    QLTO=Dept.objects.all()
    d={'dept':QLTO}
    return render(request,'dept.html',d)

def Emp(request):
    QLEO=Emp.objects.all()
    d={'name':QLEO}
    return render(request,'emp.html',d)