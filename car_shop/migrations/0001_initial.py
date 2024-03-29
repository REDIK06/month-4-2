# Generated by Django 5.0.2 on 2024-02-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите марку автомобиля')),
                ('description', models.TextField(verbose_name='Укажите  информацию о характеристиках автомобиля')),
                ('image', models.URLField(verbose_name='Укажите ссылку на фото')),
                ('year', models.CharField(max_length=100, verbose_name='Укажите год автомобиля')),
                ('engine', models.CharField(choices=[('Бензин', 'Бензин'), ('Дизель', 'Дизель'), ('Гибрид', 'Гибрид'), ('Газ', 'Газ'), ('Электро', 'Электро')], max_length=100)),
                ('steering_wheel', models.CharField(choices=[('Слева', 'Слева'), ('Справа', 'Справа')], max_length=100)),
                ('price', models.PositiveIntegerField(verbose_name='Укажите цену')),
                ('discount', models.CharField(choices=[('3%', '3%'), ('5%', '5%'), ('10%', '10%')], max_length=100)),
                ('gift', models.CharField(blank=True, max_length=100, null=True, verbose_name='Укажите подарок к покупке')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
