# Generated by Django 5.0.2 on 2024-03-06 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_product_cloth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloth',
            old_name='tile',
            new_name='title',
        ),
    ]