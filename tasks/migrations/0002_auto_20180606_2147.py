# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-06 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='status',
            field=models.CharField(choices=[('stuck', 'stuck'), ('in progress', 'in progress'), ('done', 'done'), ('cancel', 'cancel')], default='stuck', max_length=128),
        ),
    ]
