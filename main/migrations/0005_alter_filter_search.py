# Generated by Django 4.2 on 2023-07-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_filter_find_all_remove_filter_find_first_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='search',
            field=models.CharField(blank=True, default='search_all', max_length=128, null=True),
        ),
    ]
