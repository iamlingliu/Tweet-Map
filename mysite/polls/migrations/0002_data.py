# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='time published')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]
