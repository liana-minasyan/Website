# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-26 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0004_auto_20170626_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='quantity_type',
            field=models.CharField(blank=True, choices=[('եր', '-եր'), ('ներ', '-ներ')], max_length=4),
        ),
    ]
