# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0002_auto_20171125_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='pergunta',
        ),
        migrations.AddField(
            model_name='jogo',
            name='continente',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jogo',
            name='perguntasCorretas',
            field=models.IntegerField(default=0),
        ),
    ]
