# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0006_jogo_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='saldo',
        ),
        migrations.AlterField(
            model_name='jogo',
            name='usuario',
            field=models.ForeignKey(related_name='jogo_user', db_column=b'id_Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
