#registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100,required=True)
    second_name = forms.CharField(max_length=100,required=True)
    phone = forms.CharField(max_length=10,required=True)
    add = forms.CharField(max_length=200,required=True)
    dob = forms.DateField(required=True)
    #only accepting in year-month-date format rn 2006-10-25
    DATE_INPUT_FORMATS = ['%Y-%m-%d']

    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name', 'last_name', 'password1', 'password2')