# Generated by Django 5.1.2 on 2024-10-15 06:52

import banjo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swim_drill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', banjo.models.IntegerField(default=0)),
                ('instructions', banjo.models.StringField(default='')),
                ('repetitions', banjo.models.IntegerField(default=0)),
                ('difficulty', banjo.models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
