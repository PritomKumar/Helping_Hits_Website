# Generated by Django 4.1.2 on 2022-10-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_data_options_remove_data_age_remove_data_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='predictions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
