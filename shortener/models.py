from __future__ import unicode_literals

import random
import string

from django.db import models


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class KirrURLModel(models.Model):
    url = models.CharField(max_length=255)
    short_code = models.CharField(max_length=50, unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print("Save!!!!!!!!1")
        self.short_code = code_generator()
        super(KirrURLModel, self).save(force_insert=False, force_update=False, using=None,
                                       update_fields=None)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
