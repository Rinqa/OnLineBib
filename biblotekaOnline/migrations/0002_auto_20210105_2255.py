# Generated by Django 2.2.13 on 2021-01-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblotekaOnline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autori',
            name='Mbiemri',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]