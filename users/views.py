from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import User


class UserView(ListView):
    model = User
    template_name = ''
    context_object_name = ''