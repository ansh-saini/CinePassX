# Generated by Django 2.1.7 on 2019-03-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mail_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
