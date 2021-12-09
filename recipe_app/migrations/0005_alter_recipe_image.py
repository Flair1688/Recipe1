# Generated by Django 3.2.9 on 2021-11-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0004_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/recipes/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
    ]