# Generated by Django 3.2.9 on 2021-12-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0048_remove_recipe_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d', verbose_name='Аватарка')),
            ],
        ),
    ]
