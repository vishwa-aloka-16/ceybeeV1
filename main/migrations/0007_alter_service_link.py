# Generated by Django 5.1.3 on 2024-12-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_service_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.SlugField(unique=True),
        ),
    ]