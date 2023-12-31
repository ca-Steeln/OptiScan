# Generated by Django 4.2 on 2023-08-04 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_filter_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='num_keys',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='search',
            field=models.CharField(choices=[('search_all', 'search for all'), ('search_first', 'search for first'), ('search_last', 'search for last'), ('custom_search', 'custom search')], default='search_first', max_length=128, null=True),
        ),
    ]
