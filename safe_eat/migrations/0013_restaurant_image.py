# Generated by Django 5.1.2 on 2024-10-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0012_remove_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]