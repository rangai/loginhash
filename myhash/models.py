from django.conf import settings
from django.db import models

class Myhash(models.Model):
    msg = models.TextField('message', blank=False)
    hsh = models.CharField(max_length=256)

    def __str__(self):
        return self.hsh