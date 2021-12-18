from django.core.management.base import BaseCommand

from shooting1.results_viewer import show_results


class Command(BaseCommand):
    help = 'Shows shooting results for lesson1'

    def handle(self, *args, **options):
        show_results()
