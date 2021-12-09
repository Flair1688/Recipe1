# Generated by Django 3.2.9 on 2021-12-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0026_auto_20211204_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientratio',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='ingredientratio',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='tankallocation',
            name='allocation',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='name',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_title',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe_app.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preperation',
            field=models.TextField(default='Here comes the preperation...'),
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='IngredientRatio',
        ),
        migrations.DeleteModel(
            name='TankAllocation',
        ),
    ]