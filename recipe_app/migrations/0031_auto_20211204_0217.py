# Generated by Django 3.2.9 on 2021-12-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0030_auto_20211204_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.CharField(default='', max_length=150, verbose_name=models.ManyToManyField(to='recipe_app.Ingredient', verbose_name='Ингредианты')),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe_app.Ingredient', verbose_name='Ингредианты'),
        ),
    ]
