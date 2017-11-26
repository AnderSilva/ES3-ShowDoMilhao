# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0007_auto_20171126_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogo',
            old_name='usuario',
            new_name='id_usuario',
        ),
    ]
