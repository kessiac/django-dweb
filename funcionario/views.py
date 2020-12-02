from django.shortcuts import render
from django.views.generic import ListView
from . import models

class Request(ListView):

    model = models.Funcionario
    template_name = 'request.html'

class Register(ListView):

    model = models.Funcionario
    template_name = 'register.html'
