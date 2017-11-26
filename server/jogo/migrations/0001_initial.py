# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pergunta', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('saldo', models.IntegerField()),
                ('pergunta', models.ForeignKey(related_name='Jogo_Pergunta', db_column=b'id_pergunta', to='pergunta.Pergunta')),
                ('usuario', models.ForeignKey(related_name='Jogo_user', db_column=b'id_Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
