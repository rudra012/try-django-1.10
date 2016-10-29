For Django shell:
$ python manage.py shell
>>> from shortener.models import KillURLModel as km
>>> km.objects.all()

>>> new_obj=km()
>>> new_obj.url="http://www.flipkart.com/"
>>> new_obj.short_code=2342
>>> new_obj.save()


>>> obj2=km.objects.create()
>>> obj2.url="http://www.flipkart.com/"
>>> obj2.short_code=2342
>>> obj2.save()


# ModelManager Cutomization
 > from shortener.models import KirrURLModel as km
 > km.objects.all()
 > km.objects.refresh_shortcodes()
 
