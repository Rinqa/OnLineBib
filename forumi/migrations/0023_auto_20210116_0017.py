# Generated by Django 3.1.5 on 2021-01-16 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumi', '0022_auto_20210115_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Com_Autor',
        ),
        migrations.AddField(
            model_name='comment',
            name='autori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(1, 'Publik'), (2, 'Privat')], default=1),
        ),
    ]
