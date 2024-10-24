# forms.py
from django import forms
from .models import Product, Category
from django.conf import settings
from django.core.exceptions import ValidationError

wrong_word_list = settings.WRONG_WORDS_LIST


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = ""

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название категории"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['owners']
        # photo = forms.ImageField(label="Изображение")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = ""

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену"}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        # not isinstance(price, int) and
        if price <= 0:
            raise ValidationError("цена должна быть положительным целым числом")
        return price

    def clean_photo(self):
        image = self.cleaned_data.get("photo")
        if not image and image.size > 5 * 1024 * 1024:  # 5 MB
            raise ValidationError("Картинка очень большая ( > 5MB )")
        if not image and image.name.endswith(".jpg", ".jpeg", ".png"):
            raise ValidationError("Файл не является изображением")
        return image

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name and set(wrong_word_list) & set(name.lower().split()):
            self.add_error("name", "Название не может содержать запрещенные слова")
        elif description and set(wrong_word_list) & set(description.lower().split()):
            self.add_error("name", "Описание не может содержать запрещенные слова")
