# Generated by Django 2.2.13 on 2021-01-05 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0003_lendet_drejtimit_ects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(2, 'Privat'), (1, 'Publik')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='id_Lenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forumi.Lenda'),
        ),
    ]