# Generated by Django 3.0.5 on 2021-01-24 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0029_auto_20210124_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pyetje',
            old_name='pyetja',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='pergjigjje',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 1, 24, 17, 5, 11, 936211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 1, 24, 17, 5, 11, 935679, tzinfo=utc)),
        ),
    ]