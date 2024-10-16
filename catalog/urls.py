from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import (
    send,
    ProductDetailView,
    ProductsListView,
    ContactListView,
    CategoryesListView,
)
from catalog.views import (
    ProductCreateView,
    ProductUpdateView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from catalog.views import ProductModListView, ProductModDetailView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # url PROD
    path("catalog/", ProductsListView.as_view(), name="product_list"),
    path("catalog/product/all", ProductsListView.as_view(), name="products_list"),
    path("catalog/contact/", ContactListView.as_view(), name="contact"),
    path(
        "catalog/product_detail/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    # url for CRUD
    path("", ProductModListView.as_view(), name="product_mod_list"),
    path(
        "catalog/category/create", CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "catalog/category/<int:pk>/", CategoryUpdateView.as_view(), name="category_mod"
    ),
    path("catalog/category/all", CategoryesListView.as_view(), name="categoryes_list"),
    path(
        "catalog/category/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("catalog/product/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/product/<int:pk>/", ProductUpdateView.as_view(), name="product_mod"),
    path(
        "catalog/product_mod_list/",
        ProductModListView.as_view(),
        name="product_mod_list",
    ),
    path(
        "catalog/product_mod_detail/<int:pk>/",
        ProductModDetailView.as_view(),
        name="product_mod_detail",
    ),
    path(
        "catalog/product/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
