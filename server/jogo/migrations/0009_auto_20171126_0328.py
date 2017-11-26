# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0008_auto_20171126_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogo',
            old_name='perguntas_corretas',
            new_name='acertos',
        ),
        migrations.RenameField(
            model_name='jogo',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]
