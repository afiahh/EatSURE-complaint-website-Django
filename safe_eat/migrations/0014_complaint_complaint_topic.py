# Generated by Django 5.0.3 on 2024-11-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0013_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]