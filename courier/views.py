from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only




# Create your views here.
def index( request):
    if request.method == "POST":
        form =  LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        # messages.error(request, "Invalid Tracking Id")
        form = LoginForm()
    return render(request, 'index.html', {"form":form})
        



#class SignUpView(generic.CreateView):
#    form_class = UserCreationForm
#    success_url =  reverse_lazy('index')
#    template_name = "signup.html"


#def signup(request):
#    if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#                  form.save()
#            return redirect('/')
#       else:
#            form = UserCreationForm()
#        return render(request, 'signup.html', {"form":form})

def about( request):
    return render (request, 'about.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('index')

    context = {'form': form}
    return render (request, "register.html", context)


def contact( request):
    return render (request, 'contact.html')


def service( request):
    return render (request, 'service.html')   

def terms( request):
    return render (request, 'terms.html')

def blog( request):
    return render (request, 'blog.html') 

@login_required (login_url = "/")
def details( request):
    return render (request, 'details.html') 
@login_required (login_url = "/")
def receipts( request):
    return render (request, 'receipts.html') 

@login_required(login_url='/')
def home( request):
    return render (request, 'home.html')   


def logoutUser(request):
    logout (request)
    return redirect ('index')