# Generated by Django 5.1.1 on 2024-10-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="views_count",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Количество просмотров"
            ),
        ),
    ]
