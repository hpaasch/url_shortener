from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView
from hashids import Hashids

from shortener_app.models import Bookmark, Click


class IndexView(TemplateView):
    template_name = 'index_view.html'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"  # back to homepage/index view


class AccountView(ListView):  # can this show a list of URLs?
    model = User

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['author_list'] = Bookmark.objects.all()
        return context


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['url', 'title', 'description', 'private']
    template_name = 'bookmark_create.html'

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.url_user = self.request.user
        hashids = Hashids(min_length=8, salt='msnstjtnst')
        form.instance.short_code = hashids.encode(id(form.instance))
        # form.instance = form.save()  # seems not to be needed
        return super(BookmarkCreateView, self).form_valid(form)



