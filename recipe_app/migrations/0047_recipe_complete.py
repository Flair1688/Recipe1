# Generated by Django 3.2.9 on 2021-12-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0046_remove_recipe_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
