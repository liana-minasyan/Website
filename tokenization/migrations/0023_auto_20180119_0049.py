# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0022_auto_20180119_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verb',
            name='voices',
        ),
        migrations.AddField(
            model_name='verb',
            name='voice_feat',
            field=models.CharField(blank=True, choices=[('act', 'Act'), ('cau', 'Cau'), ('mid', 'Mid'), ('pass', 'Pass')], max_length=5),
        ),
        migrations.AlterField(
            model_name='verb',
            name='voice',
            field=models.CharField(choices=[('1', 'ՉԲ'), ('2', 'ՆԲ')], default='1', max_length=5),
        ),
    ]
