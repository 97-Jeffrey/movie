# Generated by Django 2.1 on 2021-01-21 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 5, 43, 44, 464570, tzinfo=utc)),
        ),
    ]
