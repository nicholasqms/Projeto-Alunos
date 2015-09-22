# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0032_remove_orientador_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientador',
            name='name',
            field=models.CharField(default='Carmen', max_length=255, verbose_name=b'Nome do Orientador'),
            preserve_default=False,
        ),
    ]
