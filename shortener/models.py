from __future__ import unicode_literals

from django.db import models

from kirr.utils import create_shortcode


class KirrURLModel(models.Model):
    url = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=50, unique=True, blank=True, null=False)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(KirrURLModel, self).save(force_insert=False, force_update=False, using=None,
                                       update_fields=None)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
