# Generated by Django 3.1.5 on 2021-01-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0017_auto_20210110_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(2, 'Privat'), (1, 'Publik')], default=1),
        ),
    ]