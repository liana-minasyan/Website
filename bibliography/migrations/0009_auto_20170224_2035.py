# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0008_press_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True, verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='fiction',
            name='text_creation_date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='fiction',
            name='text_publication_date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='press',
            name='text_publication_date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='text_creation_date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='text_publication_date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%Y-%m', '%Y', '%m']),
        ),
    ]