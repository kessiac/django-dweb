from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from . import models, forms

class UserCreateView(CreateView):

    form_class = forms.UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('users-signin')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['groups'] = Group.objects.all()
        return context
    
class FormListView(ListView):
    
    model = models.Form
    template_name = 'caest.html'

class FormProfDetailView(ListView):

    model = models.Form
    template_name = 'teacher.html'

class ReIFCreateView(CreateView):

    model = models.Form
    fields = ('professor', 'curso', 'turma', 'data', 'tipo_de_refeicao', 'alunos', 'status')
    template_name = 'request.html'
    success_url = reverse_lazy('request-list')

class ReqDetailView(DetailView):
    
    model = models.Form
    template_name = 'process.html'
