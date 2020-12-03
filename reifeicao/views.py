from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . import models

def signup(request):
    return render(request, 'register.html')
    
class FormListView(ListView):
    
    model = models.Form
    template_name = 'caest.html'

class FormDetailView(ListView):

    model = models.Form
    template_name = 'process.html'

class FormProfDetailView(ListView):

    model = models.Form
    template_name = 'teacher.html'

class Request(ListView):

    model = models.Form
    template_name = 'request.html'

class ReIFCreateView(CreateView):

    model = models.Form
    fields = ('professor', 'curso', 'turma', 'data', 'tipo_de_refeicao', 'alunos', 'status')
    template_name = 'request.html'
    success_url = reverse_lazy('request-list')