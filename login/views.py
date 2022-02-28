#users/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,"login/home.html")



class SignUp(CreateView):
    #Added feild and modified UserCreationForm for min login/forms.py
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "login/signup.html"