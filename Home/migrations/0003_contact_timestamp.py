# Generated by Django 4.1.4 on 2023-04-07 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_contact_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]