# Generated by Django 5.1.2 on 2024-10-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0004_remove_restaurant_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
