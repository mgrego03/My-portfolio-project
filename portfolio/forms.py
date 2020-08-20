

from django import forms

from .models import Skills

class SkillsForm (forms.ModelForm):
    class Meta:
        model = Skills
        fields =  [ 'skill'  , 'years'  , 'tools' ]