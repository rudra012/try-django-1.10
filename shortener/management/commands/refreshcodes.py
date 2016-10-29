from django.core.management.base import BaseCommand

from shortener.models import KirrURLModel


class Command(BaseCommand):
    help = 'Refreshes all KirrURL'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)
        # parser.add_argument('items', type=int)
        # parser.add_argument('number1', type=int)
        # parser.add_argument('number2', type=int)

    def handle(self, *args, **options):
        # print(options)
        return KirrURLModel.objects.refresh_shortcodes(options.get('items'))
