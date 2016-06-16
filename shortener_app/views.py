from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView


class IndexView(TemplateView):
    template_name = 'index_view.html'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"  # back to homepage/index view


class AccountView(ListView):
    model = User



