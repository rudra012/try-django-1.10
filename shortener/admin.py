from django.contrib import admin

from .models import KirrURLModel


@admin.register(KirrURLModel)
class KirrURLAdmin(admin.ModelAdmin):
    list_display = ['url', 'short_code', 'modified', 'created']
