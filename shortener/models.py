from __future__ import unicode_literals

from django.db import models


class KirrURLModel(models.Model):
    url = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
