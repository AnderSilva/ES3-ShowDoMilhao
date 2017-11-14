# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('avatar', models.IntegerField()),
                ('balao', models.IntegerField()),
                ('login', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('pontos', models.IntegerField()),
                ('is_admin', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
