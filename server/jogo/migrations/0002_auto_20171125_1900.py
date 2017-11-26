# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogo',
            options={'managed': True, 'verbose_name': 'jogo', 'verbose_name_plural': 'jogos'},
        ),
        migrations.AlterModelTable(
            name='jogo',
            table='jogo',
        ),
    ]
