# Generated by Django 5.0.1 on 2024-02-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_producttable_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttable',
            name='rating',
        ),
    ]
