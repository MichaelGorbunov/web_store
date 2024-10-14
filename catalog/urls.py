from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import send,ProductDetailView,ProductsListView,ContactListView,CategoryesListView
from catalog.views import ProductCreateView,ProductUpdateView,CategoryCreateView,CategoryUpdateView
app_name = CatalogConfig.name

urlpatterns = [

    path("", ProductsListView.as_view(), name="product_list"),
    path("catalog/product/all", ProductsListView.as_view(), name="products_list"),
    path("catalog/category/all", CategoryesListView.as_view(), name="categoryes_list"),
    path("catalog/contact/", ContactListView.as_view(), name="contact"),
    path("catalog/product_detail/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("catalog/product/", ProductCreateView.as_view(), name="product_mod_list"),
    path("catalog/category/", CategoryCreateView.as_view(), name="category_mod_list"),
    path("catalog/category/<int:pk>/", CategoryUpdateView.as_view(), name="category_mod"),
    path("catalog/product/<int:pk>/", ProductUpdateView.as_view(), name="product_mod")

]
