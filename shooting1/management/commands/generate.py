from django.core.management.base import BaseCommand

import random

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

        with open("shooting1/sorted_names.txt") as f:
            for name in f.readlines():
                nr = random.randint(0, 100)
                score = 150 + random.randint(0, 250)
                if 0 < nr < 90:
                    city_name = cities[0]
                else:
                    city_name = cities[random.randint(1, 7)]

                city, _ = City.objects.get_or_create(name=city_name)
                shooter, _ = Shooter.objects.get_or_create(name=name.strip(), city=city)
                Result.objects.create(shooter=shooter, result=score)
                # print(f"{name.strip().ljust(20, ' ')}\t{city.ljust(12, ' ')}\t{score}")
