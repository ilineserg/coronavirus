from django.core.management.base import BaseCommand, CommandError
from data.models import Country

import json


class Command(BaseCommand):
    help = 'Insert data to DB from XML'

    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        print(options['file'])
        with open(options['file'], 'r') as file:
            data = json.loads(file.readline())
            for i in data:
                i['name'] = i.pop('Name')
                i['alpha2'] = i.pop('Code')
                Country.objects.get_or_create(alpha2=i['alpha2'], defaults=i)
            len_data = len(data)
            len_db = len(Country.objects.all())
            if len_data == len_db:
                print('All countries match DB')
            else:
                print(f'Something wrong! \n'
                      f'Number of countries on file {len_data} != {len_db}')

