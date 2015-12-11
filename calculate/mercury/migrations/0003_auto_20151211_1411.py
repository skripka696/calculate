# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mercury', '0002_auto_20151211_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='currency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mercury.Currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='service_country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mercury.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]