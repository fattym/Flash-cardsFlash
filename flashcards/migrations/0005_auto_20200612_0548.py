# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-06-12 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20200612_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile_det',
        ),
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
