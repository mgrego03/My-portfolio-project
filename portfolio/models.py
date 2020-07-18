from django.db import models

# Create your models here.


class Project(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    from_date = models.DateField()
    to_date = models.DateField(null=True , blank = True)        # blank = True - optional ; null = True - could leave it empty

    def __str__(self):
        return self.position



class Skills (models.Model):
    skill = models.CharField(max_length = 50)
    years = models.CharField(max_length = 50)
    tools = models.TextField(max_length=500 , blank = True , null = True)

    def __str__(self):
        return self.skill


class Education (models.Model):
    Degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    Graduation_year = models.CharField(max_length=50)

    def __str__(self):
        return self.Degree