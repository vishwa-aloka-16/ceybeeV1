# Generated by Django 5.1.3 on 2024-12-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_service_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepackages',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]