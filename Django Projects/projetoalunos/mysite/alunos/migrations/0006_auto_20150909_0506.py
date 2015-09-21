# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_studentuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='identifier',
            new_name='name',
        ),
    ]
