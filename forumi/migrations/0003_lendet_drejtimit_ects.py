# Generated by Django 2.2.13 on 2021-01-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0002_auto_20210105_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendet_drejtimit',
            name='ects',
            field=models.IntegerField(default=2),
        ),
    ]
