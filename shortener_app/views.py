
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hashids import Hashids
import datetime

from shortener_app.models import Bookmark, Click


class IndexView(TemplateView):
    model = Bookmark
    template_name = 'index_view.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        public_list = Bookmark.objects.filter(private__exact=False)
        paginator = Paginator(public_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            bookmarks = paginator.page(page)
        except PageNotAnInteger:
            bookmarks = paginator.page(1)
        except EmptyPage:
            bookmarks = paginator.page(paginator.num_pages)
        context['public_bookmarks'] = bookmarks
        return context


class LinkRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        short_code = self.kwargs.get('short_code', None)
        link_url = Bookmark.objects.get(short_code=short_code)
        self.url = link_url.url
        link_url.count += 1
        link_url.save()
        Click.objects.create(url=link_url, click_time=datetime.datetime.now())
        return super(LinkRedirectView, self).get(request, args, **kwargs)


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login_view/"


class AccountView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['author_list'] = Bookmark.objects.filter(url_user__username=self.request.user)
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
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['url', 'title', 'description']
    template_name = 'bookmark_update.html'


class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('account_view')

