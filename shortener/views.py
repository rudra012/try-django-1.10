from django.http import HttpResponse
from django.views import View


def kirr_redirect_view(request, *args, **kwargs):  # function based view
    return HttpResponse("HELLO")


class KirrCBView(View):  # class based view
    def get(self, request, *args, **kwargs):
        return HttpResponse("HELLO Again")
