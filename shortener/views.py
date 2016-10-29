from django.http import HttpResponse
from django.views import View


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view
    # print(request.user)
    # print(request.user.is_authenticated())
    print(shortcode)
    print(args)
    print(kwargs)
    username = "Guest"
    if request.user.is_authenticated():
        username = request.user
    return HttpResponse("HELLO, {0} \nYour shorcode is {1}".format(username, shortcode))


class KirrCBView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)
        return kirr_redirect_view(request, shortcode, *args, **kwargs)
