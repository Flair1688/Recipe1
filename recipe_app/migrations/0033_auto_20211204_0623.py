# Generated by Django 3.2.9 on 2021-12-04 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0032_remove_recipe_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
    ]