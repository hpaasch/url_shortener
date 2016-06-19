
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from shortener_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index_view'),  # shows public links for everyone
    url(r'^register_view/$', views.RegisterView.as_view(), name='register_view'),  # register new user
    url(r'^login_view/$', login, name='login_view'),  # login existing user
    url(r'^accounts/profile/$', views.AccountView.as_view(), name='account_view'),  # all of user's links
    # url(r'^accounts/profile/clicks/$', views.ClickView.as_view(), name='click_view'),  # not used?
    url(r'^bookmark/create/$', views.BookmarkCreateView.as_view(), name='bookmark_view'),  # bookmark form
    url(r'^logout_view/$', logout, name='logout_view'),  # logout
    # url(r'^detail/$', views.LinkDetailView.as_view(), name='detail_view'),  # not used?
    url(r'^(?P<short_code>\w+)/$', views.LinkRedirectView.as_view(), name='redirect_view'),  # redirected and counted
    url(r'^update/(?P<pk>\d+)/$', views.BookmarkUpdate.as_view(), name='update_view'),  # update bookmark
    url(r'^delete/(?P<pk>\d+)/$', views.BookmarkDelete.as_view(), name='delete_view')  # delete bookmark
]
