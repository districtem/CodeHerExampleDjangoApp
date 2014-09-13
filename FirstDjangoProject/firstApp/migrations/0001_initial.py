# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CablePackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('package_name', models.CharField(max_length=255)),
                ('package_price', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('number_of_channels', models.IntegerField(null=True, blank=True)),
                ('internet_speed', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CableProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cablepackage',
            name='cable_provider',
            field=models.ForeignKey(to='firstApp.CableProvider'),
            preserve_default=True,
        ),
    ]
