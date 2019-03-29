# Generated by Django 2.1.7 on 2019-03-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190329_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dimension',
            field=models.CharField(choices=[('2d', '2D'), ('3d', '3D')], default='2d', max_length=2),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='movie_thumbnails'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('hindi', 'Hindi'), ('english', 'English')], max_length=10),
        ),
    ]