from django import forms
from datetime import date
from catalog.models import Contact, Product, Category
# форма для добавления в БД новых авторов
class Form_Add_Product(forms.Form):
    name = forms.CharField(label="Наименование")
    description = forms.CharField(label="Описание")
    photo = forms.ImageField(label="Фото продукта")
    category=forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(),empty_label=None)


