# Generated by Django 3.1.5 on 2021-01-16 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0024_auto_20210116_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postimi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forumi.postimet'),
        ),
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(1, 'Publik'), (2, 'Privat')], default=1),
        ),
    ]
