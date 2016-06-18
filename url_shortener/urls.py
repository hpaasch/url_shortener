
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from shortener_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index_view'),  # needs to show objects from db
    url(r'^register_view/$', views.RegisterView.as_view(), name='register_view'),
    url(r'^login_view/$', login, name='login_view'),
    url(r'^accounts/profile/$', views.AccountView.as_view(), name='account_view'),
    url(r'^bookmark/create/$', views.BookmarkCreateView.as_view(), name='bookmark_view'),
    url(r'^logout_view/$', logout, name='logout_view'),
    url(r'^b/(?P<short_code>\w+)/$', views.RedirectURLView.as_view(), name='redirect_view')
]
