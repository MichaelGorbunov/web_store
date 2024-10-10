# Generated by Django 5.1.1 on 2024-10-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_job_interval"),
    ]

    operations = [
        migrations.CreateModel(
            name="CronJob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_id", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=200)),
                ("minute", models.CharField(default="*", max_length=10)),
                ("hour", models.CharField(default="*", max_length=10)),
                ("day", models.CharField(default="*", max_length=10)),
                ("month", models.CharField(default="*", max_length=10)),
                ("day_of_week", models.CharField(default="*", max_length=10)),
            ],
        ),
    ]
