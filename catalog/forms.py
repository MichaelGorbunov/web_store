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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



    def clean_price(self):
        price = self.cleaned_data.get('price')
        # not isinstance(price, int) and
        if  price<=0:
            raise ValidationError('цена должна быть положительным целым числом')

        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name  and set(wrong_word_list) & set(name.lower().split()):
            self.add_error('name', 'Название не может содержать запрещенные слова')
        elif  description and set(wrong_word_list) & set(description.lower().split()):
            self.add_error('name', 'Описание не может содержать запрещенные слова')
