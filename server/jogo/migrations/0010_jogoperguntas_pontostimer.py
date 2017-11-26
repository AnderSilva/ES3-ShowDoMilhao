# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pergunta', '__first__'),
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
        migrations.CreateModel(
            name='JogoPerguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acertou', models.BooleanField()),
                ('jogo', models.ForeignKey(related_name='jogo_perguntas', to='jogo.Jogo')),
                ('pergunta', models.ForeignKey(related_name='perguntas_jogo', db_column=b'id_pergunta', to='pergunta.Pergunta')),
            ],
            options={
                'db_table': 'jogo_pergunta',
                'managed': True,
            },
        ),
    ]
