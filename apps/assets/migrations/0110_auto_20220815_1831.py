# Generated by Django 3.2.14 on 2022-08-15 10:31

import common.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0109_auto_20220815_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='token',
            field=common.db.fields.EncryptTextField(blank=True, null=True, verbose_name='Token'),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='token',
            field=common.db.fields.EncryptTextField(blank=True, null=True, verbose_name='Token'),
        ),
    ]
