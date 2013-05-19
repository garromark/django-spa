from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User)
    url = models.CharField(max_length=500)

    def __unicode__(self):
        return self.url
