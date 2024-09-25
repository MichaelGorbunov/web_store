from django import forms
from datetime import date
from catalog.models import Contact, Product, Category

class Form_Add_Product(forms.Form):
    name = forms.CharField(label="Наименование")
    description = forms.CharField(label="Описание")
    price = forms.IntegerField(label="Цена",min_value=0,step_size=None)
    # photo = forms.ImageField(label="Фото продукта")
    category=forms.ModelChoiceField(queryset=Category.objects.order_by("name"), widget=forms.Select(),empty_label=None,label="Категория")


