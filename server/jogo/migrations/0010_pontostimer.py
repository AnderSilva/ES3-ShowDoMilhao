# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0009_auto_20171126_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontosTimer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ate_segundos', models.IntegerField()),
                ('pontos', models.IntegerField()),
            ],
            options={
                'db_table': 'pontos_timer',
                'managed': False,
            },
        ),
    ]
