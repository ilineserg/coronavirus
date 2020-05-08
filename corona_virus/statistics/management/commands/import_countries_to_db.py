from django.core.management.base import BaseCommand, CommandError
from countries.models import Country

import json


class Command(BaseCommand):
    help = 'Insert data to DB from json'

    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):

        with open(options['file'], 'r') as f:
            data = json.load(f)
            for code, name in data.items():
                Country.objects.get_or_create(
                    iso_alpha2=code,
                    defaults={'name': name}
                )
