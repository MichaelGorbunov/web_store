# Generated by Django 5.1.1 on 2024-10-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [("can_unpublish_product", "Сan unpublish product")],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="allowed_publication",
            field=models.BooleanField(
                default=False,
                help_text="Этот продукт разрешен для публикации",
                verbose_name="Разрешение для публикации",
            ),
        ),
    ]
