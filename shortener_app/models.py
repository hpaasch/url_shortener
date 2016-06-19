from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)  # makes this optional
    created = models.DateTimeField(auto_now_add=True)
    url_user = models.ForeignKey(User)
    short_code = models.CharField(max_length=25)
    private = models.BooleanField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('account_view')


class Click(models.Model):
    url = models.ForeignKey(Bookmark)
    click_time = models.DateTimeField()

    class Meta:
        ordering = ['-click_time']

    def __str__(self):
        return self.url.title
