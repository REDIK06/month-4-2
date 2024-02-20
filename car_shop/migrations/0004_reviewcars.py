# Generated by Django 5.0.2 on 2024-02-17 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_shop', '0003_carshop_acceleration_alter_carshop_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.DateTimeField(verbose_name='Напишите комент')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_cars', to='car_shop.carshop')),
            ],
        ),
    ]