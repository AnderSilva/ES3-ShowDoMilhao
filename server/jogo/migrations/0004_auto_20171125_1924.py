# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0003_auto_20171125_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogo',
            old_name='lastUpdate',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='jogo',
            old_name='perguntasCorretas',
            new_name='perguntas_corretas',
        ),
    ]
