# Generated by Django 3.0.5 on 2020-04-10 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200410_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='alpha3',
        ),
        migrations.RemoveField(
            model_name='country',
            name='english_name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='country',
            name='location',
        ),
        migrations.RemoveField(
            model_name='country',
            name='location_precise',
        ),
    ]
