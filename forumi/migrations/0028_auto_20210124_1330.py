# Generated by Django 3.0.5 on 2021-01-24 13:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumi', '0027_auto_20210119_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(2, 'Privat'), (1, 'Publik')], default=1),
        ),
        migrations.CreateModel(
            name='pyetje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyetja', models.CharField(max_length=500)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('data', models.DateField(default=datetime.datetime(2021, 1, 24, 13, 30, 53, 507962, tzinfo=utc))),
                ('autori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('drejtimetEfakultetit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumi.drejtimetEfakultetit')),
            ],
        ),
        migrations.CreateModel(
            name='pergjigjje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergjigja', models.CharField(max_length=1000)),
                ('data', models.DateField(default=datetime.datetime(2021, 1, 24, 13, 30, 53, 508485, tzinfo=utc))),
                ('autori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pyetje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumi.pyetje')),
            ],
        ),
    ]
