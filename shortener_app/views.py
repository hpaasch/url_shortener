from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView

from shortener_app.models import Bookmark, Click


class IndexView(TemplateView):
    template_name = 'index_view.html'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"  # back to homepage/index view


class AccountView(ListView):
    model = User


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['url', 'title', 'description', 'private']
    template_name = 'auth/user_list.html'

    def form_valid(self, form):
        form.instance.url_user = self.request.user
        # bookmark = form.save(commit=False)
        # bookmark.created_by = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

