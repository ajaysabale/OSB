# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked_slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('timing', models.CharField(max_length=20)),
                ('count', models.IntegerField(default=100)),
            ],
        ),
        migrations.AddField(
            model_name='booked_slot',
            name='event',
            field=models.ForeignKey(to='OSB.Events'),
        ),
        migrations.AddField(
            model_name='booked_slot',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
