# Generated by Django 2.2.6 on 2019-10-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingItems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]