"""if URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from reifeicao import views
from django.conf import settings
from funcionario import views as viewsfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.FormListView.as_view()),
    path('process/', views.FormDetailView.as_view()),
    path('professor/', views.FormProfDetailView.as_view()),
    path('request/', viewsfunc.Request.as_view()),
    path('register/', viewsfunc.Register.as_view()),
    path('login/', views.index, name='login'),
    path('', views.index, name='index'),

    #path('register/', views.register_page),
]
urlpatterns += staticfiles_urlpatterns()


