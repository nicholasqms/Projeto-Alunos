# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0033_orientador_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentUser',
        ),
        migrations.DeleteModel(
            name='TeacherUser',
        ),
    ]
