# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_alternativa', models.IntegerField()),
                ('alternativa', models.CharField(max_length=1000)),
                ('resposta', models.TextField()),
                ('frequencia', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'alternativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id_pergunta', models.IntegerField(serialize=False, primary_key=True)),
                ('pergunta', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'pergunta',
                'managed': False,
            },
        ),
    ]
