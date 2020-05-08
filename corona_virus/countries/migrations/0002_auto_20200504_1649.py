# Generated by Django 3.0.5 on 2020-05-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='iso_alpha2',
            field=models.CharField(max_length=10, unique=True, verbose_name='ISO Alpha2'),
        ),
    ]
