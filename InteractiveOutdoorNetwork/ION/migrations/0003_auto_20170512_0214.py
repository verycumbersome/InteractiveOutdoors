# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ION', '0002_auto_20170511_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
        migrations.AlterField(
            model_name='gearpost',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]