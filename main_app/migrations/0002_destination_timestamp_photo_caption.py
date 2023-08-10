# Generated by Django 4.2.3 on 2023-08-10 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="destination",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="photo",
            name="caption",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
