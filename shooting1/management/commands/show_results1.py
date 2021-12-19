from django.core.management.base import BaseCommand
from texttable import Texttable

from django.utils.module_loading import import_string


class Command(BaseCommand):
    help = 'Shows shooting results for lesson1'

    def add_arguments(self, parser):
        parser.add_argument('get_results_function', type=str)
        return parser

    def handle(self, *args, **options):
        results_provider = import_string("shooting1.{}".format(options["get_results_function"]))
        results = results_provider()
        table = Texttable()
        table.add_row(["Место", "Город", "Стрелок", "Результат"])
        for idx, res in enumerate(results):
            table.add_row([idx+1, res.shooter.city.name, res.shooter.name, res.score])
        print(table.draw())
