


from django.contrib import admin
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [

    path('', views.home , name = 'home') ,

    # to add a new skill from front end
    path('add/', views.create_item ,  name='create_item' ) ,

    # to update the skills from the front end: update/id of the skill
    path('update/<int:id>/' , views.update_skill , name ='update_skill') ,

    # to delete a skill
    path('delete/<int:id>/' , views.delete_skill , name = 'delete_skill') ,



]
