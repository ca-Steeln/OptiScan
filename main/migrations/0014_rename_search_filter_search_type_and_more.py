# Generated by Django 4.2 on 2023-08-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_filter_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='search',
            new_name='search_type',
        ),
        migrations.AddField(
            model_name='filter',
            name='search_behavior',
            field=models.CharField(choices=[('full_match', 'Full Match'), ('start_match', 'Start Match'), ('end_match', 'End Match'), ('all_match', 'All Match')], default='full_match', max_length=128, null=True),
        ),
    ]
