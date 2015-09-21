# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0006_auto_20150909_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b"Teacher's Name")),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('department', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
