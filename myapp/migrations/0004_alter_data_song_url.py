# Generated by Django 4.1.2 on 2022-10-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_data_predictions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="song_url",
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
