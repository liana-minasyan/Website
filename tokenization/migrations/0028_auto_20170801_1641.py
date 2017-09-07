# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-01 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0027_verb_ending'),
    ]

    operations = [
        migrations.AddField(
            model_name='noun',
            name='animate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noun',
            name='nominalized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noun',
            name='plural_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noun',
            name='uncountable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='selected_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_tag', to='tokenization.Word'),
        ),
    ]
