# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0010_auto_20150914_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacheruser',
            name='department',
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='CPF',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='contact',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='email',
            field=models.CharField(default=b'your_email@service.com', max_length=100),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='register_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
