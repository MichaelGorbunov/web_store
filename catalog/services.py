# services.py
from .models import Product,Category


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
        return Product.objects.filter(category=category)




