# Generated by Django 5.1.2 on 2024-10-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0010_rename_restaurantname_complaint_restaurant_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
