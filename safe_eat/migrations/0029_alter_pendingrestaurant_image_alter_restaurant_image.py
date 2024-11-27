# Generated by Django 5.0.2 on 2024-11-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0028_alter_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingrestaurant',
            name='image',
            field=models.ImageField(blank=True, default='static/images/no_logo.jpg', null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, default='static/images/no_logo.jpg', null=True, upload_to='static/images'),
        ),
    ]
