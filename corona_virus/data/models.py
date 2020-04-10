from django.db import models


class Country(models.Model):
    name = models.TextField(name='name', unique=True, blank=False, null=False)
    alpha2 = models.TextField(name='alpha2',
                              unique=True, blank=False, null=False)
    region = models.TextField(name='region', blank=False, null=True)


class StatisticCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    day = models.DateField(name='day', auto_now=False, auto_now_add=False)
    deaths = models.IntegerField(name='deaths')
    cumulative_deaths = models.IntegerField(name='cumulative_deaths')
    confirmed = models.IntegerField(name='confirmed')
    cumulative_confirmed = models.IntegerField(name='cumulative_confirmed')
    created = models.DateTimeField(name='created')
