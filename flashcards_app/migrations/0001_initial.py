# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='date and time added Answer')),
                ('image', models.ImageField(upload_to='', verbose_name='image to answer')),
                ('content_1', models.TextField(max_length=10000, verbose_name='content 1')),
                ('sentence_1', models.TextField(max_length=10000, verbose_name='sentences to content 1')),
                ('content_2', models.TextField(max_length=10000, verbose_name='content 2')),
                ('sentence_2', models.TextField(max_length=10000, verbose_name='sentences to content 2')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='group name')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dont_know', models.ManyToManyField(related_name='unknownquestions', to='flashcards_app.Content')),
                ('know', models.ManyToManyField(related_name='knownquestions', to='flashcards_app.Content')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards_app.Content')),
                ('to_repeat', models.ManyToManyField(related_name='questionstorepeat', to='flashcards_app.Content')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='group',
            field=models.ManyToManyField(related_name='groupquestion', to='flashcards_app.Group', verbose_name='group of question'),
        ),
        migrations.AddField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]