# Generated by Django 4.2.9 on 2024-01-27 11:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bilets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilets',
            name='invoiceId',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
