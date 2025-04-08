from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username  = forms.CharField(max_length=200, label="Full Name", widget=forms.TextInput(attrs={"placeholder":'Enter Your Full Name'}))
    password = forms.CharField(max_length=255, label="Tracking ID", widget=forms.TextInput(attrs={"placeholder":'Enter Your Tracking id'}))
    
    class Meta:
        fields= ("password")

       
       
class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class ProductForm (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user']


class TrackingForm (ModelForm):
    class Meta:
        model = Tracking
        fields = '__all__'
        exclude = ['user']


class Map_ImageForm (ModelForm):
    class Meta:
        model = Map_Image
        fields = '__all__'
        exclude = ['user']