# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-28 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0015_auto_20170626_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='bibliography',
            name='tagged',
            field=models.CharField(choices=[('no', 'Թագավորված չէ'), ('yes', 'Թագավորված է'), ('validated', 'Թագավորված է, ստուգված է')], default='no', max_length=20),
        ),
    ]
