from django.core.management.base import BaseCommand
from populate_data import populate_data


class Command(BaseCommand):
    help = 'Filling data base...'

    def handle(self, *args, **kwargs):
        populate_data()
