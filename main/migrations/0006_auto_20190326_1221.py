# Generated by Django 2.1.7 on 2019-03-26 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190326_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.TimeField(),
        ),
    ]