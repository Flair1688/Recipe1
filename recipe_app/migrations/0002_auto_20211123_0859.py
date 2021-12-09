# Generated by Django 3.2.9 on 2021-11-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='number',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(blank=True, upload_to='recipe_app/images'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='recipe_app/videos/', verbose_name=''),
        ),
    ]