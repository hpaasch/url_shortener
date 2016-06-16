
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from shortener_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index_view'),  # needs to show something
    url(r'^register_view/$', views.RegisterView.as_view(), name='register_view'),
    url(r'^login_view/$', login, name='login_view'),
    url(r'^logout_view/$', logout, name='logout_view'),
]
