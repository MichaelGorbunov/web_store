# services.py
from .models import Product

class ProductService:
    @staticmethod
    def get_prod_from_cat(cat_id):
        # Получаем все продукты в категории
        products = Product.objects.filter(category=cat_id)
        return products
