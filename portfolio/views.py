from django.shortcuts import render , redirect

# Create your views here.
from portfolio.models import Project
from portfolio.models import Skills
from portfolio.models import Education
from .forms import SkillsForm



def home(request):
    projects = Project.objects.all()
    skills = Skills.objects.all()
    education = Education.objects.all()
    return render(request , 'portfolio/home.html' , {'projects' : projects , 'skills' : skills , 'education':education})


def create_item(request):
    form = SkillsForm(request.POST or None)

    if form .is_valid():
        form.save()
        return redirect('portfolio:home')


    return render(request ,  'portfolio/skills_form.html' , {'form':form})


def update_skill(request,id):
    item = Skills.objects.get(id=id)
    form = SkillsForm(request.POST or None , instance=item)     # the already existing skill should already be in the form

    if form .is_valid():
        form.save()
        return redirect('portfolio:home')

    return render(request , 'portfolio/skills_form.html' ,  {'form':form , 'item':item})



def delete_skill(request , id):
    item = Skills.objects.get(id=id)         # item we want to delete by its id    ( create an object of the Skills class )

    if request.method == 'POST':      # if it is a post method, we delete the item
        item.delete()
        return redirect('portfolio:home')

    return render(request , 'portfolio/skills_delete.html' , {'item':item} )       # to confirm the deletion