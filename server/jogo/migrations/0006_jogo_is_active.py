# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0005_auto_20171125_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
