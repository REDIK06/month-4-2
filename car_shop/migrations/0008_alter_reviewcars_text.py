# Generated by Django 5.0.2 on 2024-03-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_shop', '0007_comment_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcars',
            name='text',
            field=models.TextField(verbose_name='Напишите коммент'),
        ),
    ]
