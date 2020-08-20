from django.shortcuts import render , redirect
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# we will create the form from usercreationform

#from .forms import RegisterForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':       # if a post request, user clicked signup in the template
        form = UserCreationForm(request.POST)     # will have all the data that was submitted with the form
        if form.is_valid():       # check if the form data retrieved is valid
            form.save()        # save user to database
            username = form.cleaned_data.get('username')   # we want to get the name that was entered into username field from the form
            messages.success(request , f'welcome {username}, your account is created')
            return redirect('login')          # this will redirect this to the login page ( check the urls.py to see the login url)

    else:
        form  = UserCreationForm()      # if the signup button is not pressed

    return render (request ,   'users/register.html'  , {'form':form})      # we want to pass the inbuild from to the template register.html



# we want to restrict access to the profile page if user is logedout , so we add a decorator

@login_required
def profilepage(request):
    return render(request , 'users/profile.html' )