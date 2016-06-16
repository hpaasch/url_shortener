from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView


class IndexView(View):
    # template_name = 'index_view.html'
    #
    # def get_context_data(self, **kwargs):
    #     context['name'] = 'hi hope'
    #     return context
    def get(self, request):
        return HttpResponse('Welcome to URL shortener')

class RegisterView(CreateView):  # creates a user
    model = User
    form_class = UserCreationForm
    # success_url = "/"  # back to homepage/index view
