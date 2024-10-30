# services.py
from .models import Product,Category
from django.conf import settings
from django.core.cache import cache


class ProductService:
    @staticmethod
    def get_prod_from_cat(cat_id):
        # Получаем все продукты в категории
        products = Product.objects.filter(category=cat_id)
        return products

    @staticmethod
    def get_all_categories():
        """выбор категорий"""
        return Category.objects.all()

    @staticmethod
    def get_product_by_category(category):
        """продукты в категории"""
        if settings.CACHES_ENABLED:
            key = "products"
            products=cache.get(key)
            if products is None:
                products=Product.objects.all()
                cache.set(key, products, 3600)
        else:
            products = Product.objects.get.all()

        return products.filter(category=category)




