# Generated by Django 3.1.5 on 2021-01-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0015_auto_20210108_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(2, 'Privat'), (1, 'Publik')], default=1),
        ),
    ]