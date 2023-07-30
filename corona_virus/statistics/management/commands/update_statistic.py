import requests
from itertools import groupby

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from countries.models import Country
from statistics.models import CountryStatistic


class Command(BaseCommand):
    help = 'Insert actual data to DB from actual json'

    def add_arguments(self, parser):
        # parser.add_argument('--file', '-f', type=str)
        pass

    def handle(self, *args, **options):
        session = requests.Session()
        r = session.get(settings.COVID_DATA_URL)
        r.raise_for_status()

        data = r.json()
        rows = data.get('rows')

        assert rows, 'No data in response'

        errors = []

        sorted_rows = sorted(rows, key=lambda x: x[1])
        groups = groupby(sorted_rows, key=lambda x: x[1])

        for key, rows in groups:
            country = Country.objects.filter(iso_alpha2=key).first()

            if not country:
                errors.append(
                    f"Country with ISO code alpha2 '{key}' doesn't exists!")
                continue

            print(country.name)

            rows = list(sorted(rows, key=lambda x: x[0]))

            date_rows = {
                timezone.datetime.fromtimestamp(row[0]/1000).date(): row
                for row in rows
            }

            statistics_exist = CountryStatistic.objects.filter(
                country=country,
                date__in=date_rows.keys()
            )

            print(f'Exists {statistics_exist.count()}')

            for stat in statistics_exist:
                _data = date_rows.pop(stat.date)
                stat.deaths = _data[3]
                stat.cumulative_deaths = _data[4]
                stat.confirmed = _data[5]
                stat.cumulative_confirmed = _data[6]

            CountryStatistic.objects.bulk_update(
                statistics_exist,
                fields=['deaths', 'cumulative_deaths',
                        'confirmed', 'cumulative_confirmed']
            )

            for date, row in date_rows.items():

                CountryStatistic.objects.create(
                    country=country,
                    date=date,
                    deaths=row[3],
                    cumulative_deaths=row[4],
                    confirmed=row[5],
                    cumulative_confirmed=row[6],
                )

        print('\n'.join(errors))
