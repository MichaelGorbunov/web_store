from django.contrib import admin
from catalog.models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("country", "tax_reg_number", "address", "phone")
