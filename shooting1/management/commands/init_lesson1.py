from django.core.management import call_command
from django.core.management.base import BaseCommand

from shooting1.models import Shooter, City, Result

cities = [
    'Москва',
    'Спб',
    'Ростов',
    'Новосибирск',
    'Омск',
    'Томск',
    'Ижевск',
    'Тула'
]


class Command(BaseCommand):
    help = 'Shows shooting results for lesson1'

    def handle(self, *args, **options):
        Result.objects.all().delete()
        Shooter.objects.all().delete()
        City.objects.all().delete()

        call_command('loaddata', 'cities.json', app_label='shooting1', verbosity=0)
        call_command('loaddata', 'shooters.json', app_label='shooting1', verbosity=0)
        call_command('loaddata', 'results.json', app_label='shooting1', verbosity=0)
