from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from kirr.utils import create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)



class KirrURLModelManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLModelManager, self).all(*args, **kwargs)
        qs = qs_main.filter(is_active=True)
        print(qs)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURLModel.objects.filter(id__gte=1)
        if items and isinstance(items, int):
            qs = qs.order_by("-id")[:items]

        new_code_count = 0
        for q in qs:
            q.shorcode = create_shortcode(q)
            new_code_count += 1
            q.save()
            print("ID: {0} ==> {1}".format(q.id, q.shorcode))
        return "New codes made: {0}".format(new_code_count)


class KirrURLModel(models.Model):
    url = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True, null=False)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = KirrURLModelManager()

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
