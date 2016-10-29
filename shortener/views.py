from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from shortener.models import KirrURLModel


def test_view(request, shortcode=None, *args, **kwargs):  # function based view
    return HttpResponse("TEST View")


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view

    print(shortcode)
    obj = get_object_or_404(KirrURLModel, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
    # return HttpResponse("Your shorcode is {sc}\n URL: {url}".format(sc=shortcode, url=obj.url))


class KirrCBView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        return kirr_redirect_view(request, shortcode, *args, **kwargs)


'''

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view
    # print(request.user)
    # print(request.user.is_authenticated())
    # print(shortcode)
    # print(args)
    # print(kwargs)
    username = "Guest"
    if request.user.is_authenticated():
        username = request.user

    # obj_url = None
    # qs = KirrURLModel.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     qs = qs.first()
    #     obj_url = qs.url

    obj = get_object_or_404(KirrURLModel, shortcode=shortcode)
    # obj_url=obj.url

    return HttpResponse("HELLO, {0} \nYour shorcode is {1}\n URL: {2}".format(username, shortcode, obj.url))


'''
