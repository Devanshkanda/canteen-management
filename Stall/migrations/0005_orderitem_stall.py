# Generated by Django 4.2.1 on 2023-05-21 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stall', '0004_order_orderitem_deliveryinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='stall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stall.stall'),
        ),
    ]
