# Generated by Django 4.1.4 on 2022-12-10 04:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.FloatField()),
                ('f_codedesc', models.CharField(max_length=80)),
                ('f_code', models.CharField(max_length=80)),
                ('areakm2', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
