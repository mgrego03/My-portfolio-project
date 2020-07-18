from django.db import models

# Create your models here.

class Allprojecct (models.Model):
    project_name = models.CharField(max_length=50)
    project_desc = models.TextField(max_length=1000)
    project_url = models.URLField(blank = True , null = True)
    project_tech = models.TextField(max_length=500)



    def __str__(self):
        return self.project_name