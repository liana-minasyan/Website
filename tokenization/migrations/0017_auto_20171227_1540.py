# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0016_auto_20171217_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verb',
            name='demq',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='ending',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='form',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='root',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='type',
        ),
        migrations.AddField(
            model_name='verb',
            name='aspect',
            field=models.CharField(blank=True, choices=[('dur', 'Dur'), ('imp', 'Imp'), ('iter', 'Iter'), ('perf', 'Perf'), ('prosp', 'Prosp')], max_length=7),
        ),
        migrations.AddField(
            model_name='verb',
            name='mood',
            field=models.CharField(blank=True, choices=[('cnd', 'Conditional'), ('imp', 'Imperative'), ('ind', 'Indicative'), ('nec', 'Necessitative'), ('sub', 'Subjunctive')], max_length=4),
        ),
        migrations.AddField(
            model_name='verb',
            name='number',
            field=models.CharField(blank=True, choices=[('singular', 'Singular'), ('plural', 'Plural'), ('collective', 'Collective'), ('assocpl', 'Associative')], max_length=13),
        ),
        migrations.AddField(
            model_name='verb',
            name='person',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=3),
        ),
        migrations.AddField(
            model_name='verb',
            name='polarity',
            field=models.CharField(blank=True, choices=[('neg', 'Neg'), ('pos', 'Pos')], max_length=4),
        ),
        migrations.AddField(
            model_name='verb',
            name='poss_number',
            field=models.CharField(blank=True, choices=[('sing', 'Sing'), ('plur', 'Plur')], max_length=5),
        ),
        migrations.AddField(
            model_name='verb',
            name='poss_person',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=3),
        ),
        migrations.AddField(
            model_name='verb',
            name='subcat',
            field=models.CharField(blank=True, choices=[('intr', 'Intransitive'), ('tran', 'Transitive')], max_length=5),
        ),
        migrations.AddField(
            model_name='verb',
            name='tense',
            field=models.CharField(blank=True, choices=[('imp', 'Imp'), ('past', 'Past'), ('pres', 'Pres')], max_length=5),
        ),
        migrations.AddField(
            model_name='verb',
            name='verb_form',
            field=models.CharField(blank=True, choices=[('conv', 'Conv'), ('fin', 'Fin'), ('inf', 'Inf'), ('part', 'Part')], max_length=5),
        ),
        migrations.AddField(
            model_name='verb',
            name='voice',
            field=models.CharField(blank=True, choices=[('act', 'Act'), ('cau', 'Cau'), ('mid', 'Mid'), ('pass', 'Pass')], max_length=5),
        ),
    ]