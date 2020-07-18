from django.contrib import admin

# Register your models here.


from .models import Project         #    import the Project class
from .models import Skills
from .models import Education


admin.site.register(Project)

admin.site.register(Skills)

admin.site.register(Education)