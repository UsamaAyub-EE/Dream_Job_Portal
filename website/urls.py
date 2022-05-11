"""CEP_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("index", views.index),
    path("add_company", views.add_company),
    path("add_business_stream", views.add_business_stream),
    path("add_job", views.add_job),
    path("add_job_seeker", views.add_job_seeker),
    path("add_education_detail", views.add_education_detail),
    path("add_experience_detail", views.add_experience_detail),
    path("job_seeker_login", views.job_seeker_login),
    path("apply_for_job", views.apply_for_job),
    path("job_seeker_page", views.job_seeker_page),
    path("add_job_type", views.add_job_type),
    path("company_login", views.company_login),
    path("job_search", views.job_search),
    path("admin_login", views.admin_login),
    path("admin_page", views.admin_page),
]
