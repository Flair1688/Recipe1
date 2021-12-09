# Generated by Django 3.2.9 on 2021-12-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0028_auto_20211204_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, to='recipe_app.Ingredient', verbose_name='Ингредианты'),
        ),
    ]
