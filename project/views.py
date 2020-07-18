from django.shortcuts import render

# Create your views here.
from .models import Allprojecct


def all_project(request):
    allprojects = Allprojecct.objects.all()
    return render(request , 'project/all_project.html' , {'Allprojects' : allprojects})