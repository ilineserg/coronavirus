from django.db import models


class CountryStatistic(models.Model):
    country = models.ForeignKey(
        'countries.Country', on_delete=models.CASCADE, verbose_name='Country'
    )
    date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Date')
    deaths = models.IntegerField(
        null=True, verbose_name='Deaths'
    )
    cumulative_deaths = models.IntegerField(
        null=True, verbose_name='Cumulative deaths'
    )
    confirmed = models.IntegerField(
        null=True, verbose_name='Confirmed'
    )
    cumulative_confirmed = models.IntegerField(
        null=True, verbose_name='Cumulative confirmed'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated at'
    )

    class Meta:
        unique_together = ('country', 'date')
        db_table = 'statistic'
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'
