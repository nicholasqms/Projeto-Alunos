# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0015_auto_20150914_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='username',
            field=models.CharField(default=b'Username Here', unique=True, max_length=30, verbose_name=b'Username'),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='username',
            field=models.CharField(default=b'Username Here', unique=True, max_length=30, verbose_name=b'Username'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b"Student's Name"),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b"Teacher's Name"),
        ),
    ]
