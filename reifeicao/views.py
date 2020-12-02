from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views.generic import ListView
from . import models

def index(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.radio_choices == "Professor(a)":
        return render(request, 'teacher.html')
    return render(request, "register.html", context)
    
class FormListView(ListView):
    
    model = models.Form
    template_name = 'caest.html'

class FormDetailView(ListView):

    model = models.Form
    template_name = 'process.html'

class FormProfDetailView(ListView):

    model = models.Form
    template_name = 'teacher.html'
