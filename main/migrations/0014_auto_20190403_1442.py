# Generated by Django 2.1.7 on 2019-04-03 09:12

from django.db import migrations, models
import django_imgur.storage


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190331_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, storage=django_imgur.storage.ImgurStorage(), upload_to='movie_thumbnails'),
        ),
    ]