# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='sentence_1',
            field=models.TextField(blank=True, max_length=10000, verbose_name='sentences to content 1'),
        ),
    ]