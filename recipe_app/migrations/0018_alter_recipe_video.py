# Generated by Django 3.2.9 on 2021-12-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0017_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos//%Y/%m/%d', verbose_name=''),
        ),
    ]
