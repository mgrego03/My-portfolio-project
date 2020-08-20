

from django import forms

from django.contrib.auth.models import User
 # above user model is already build into django

from django.contrib.auth.forms import UserCreationForm


 # we are creating a new form because we also want to get the email address of the user
 # when they signup. the usercreationform does not have an email field.
 # so we create a new form with email field and then inherit from usercreationform

 # create the new form
class RegisterForm(UserCreationForm):
     email = forms.EmailInput()

     class Meta:                    #  meaning that this meta class will hold info about the registrationform class above
         model = User
         fields = ['username' , 'email' , 'password1' , 'password2' ]
