from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=500, unique=True,
        verbose_name='Name'
    )
    iso_alpha2 = models.CharField(
        max_length=10, unique=True,
        verbose_name='ISO Alpha2'
    )
    # iso_alpha3 = models.CharField(
    #     max_length=10, unique=True, blank=True, null=True,
    #     verbose_name='ISO Alpha3'
    # )
    region = models.CharField(
        max_length=10, blank=False, null=True,
        verbose_name='Region'
    )

    class Meta:
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
