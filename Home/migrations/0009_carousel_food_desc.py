# Generated by Django 4.1.4 on 2023-05-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_carousel_food_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='food_desc',
            field=models.CharField(default='Mouth watering', max_length=100),
        ),
    ]
