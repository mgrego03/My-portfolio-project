from django.shortcuts import render

# Create your views here.
from portfolio.models import Project
from portfolio.models import Skills
from portfolio.models import Education



def home(request):
    projects = Project.objects.all()
    skills = Skills.objects.all()
    education = Education.objects.all()
    return render(request , 'portfolio/home.html' , {'projects' : projects , 'skills' : skills , 'education':education})
