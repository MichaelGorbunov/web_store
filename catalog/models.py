from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        default="photos/default.jpg",
        verbose_name="Изображение (превью)",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию",
        related_name="categories",
    )
    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Цена",
        help_text="Укажите цену за покупку"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания (записи в БД)",
        help_text="Укажите дату создания (записи в БД)",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения (записи в БД)",
        help_text="Укажите дату последнего изменения (записи в БД)",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    country = models.CharField(
        default="Российская Федерация",
        max_length=50,
        verbose_name="Страна",
        help_text="Введите наименование страны",
    )
    tax_reg_number = models.CharField(
        max_length=12,
        verbose_name="ИНН",
        help_text="Введите номер налогоплательщика",
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=250,
        verbose_name="Адрес",
        help_text="Введите адрес",
    )
    phone = models.CharField(
        max_length=12,
        verbose_name="Основной телефон",
        help_text="Введите номер телефона",
    )
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.address