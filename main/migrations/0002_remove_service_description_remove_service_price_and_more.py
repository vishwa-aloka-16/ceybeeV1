# Generated by Django 5.1.3 on 2024-12-25 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.CreateModel(
            name='servicePackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
        ),
        migrations.CreateModel(
            name='packageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('servicePackage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicepackages')),
            ],
        ),
        migrations.DeleteModel(
            name='serviceDetails',
        ),
    ]