# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0004_auto_20171125_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='continente',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
