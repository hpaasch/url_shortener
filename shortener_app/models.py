from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Click(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)  # makes this optional
    created = models.DateTimeField(auto_now_add=True)
    url_user = models.ForeignKey(User)
    short_code = models.CharField(max_length=25)
    private = models.NullBooleanField()

    def __str__(self):
        return self.title

