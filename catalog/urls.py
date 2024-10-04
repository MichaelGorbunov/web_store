from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import send,ProductDetailView,ProductsListView,ContactListView

app_name = CatalogConfig.name

urlpatterns = [

    path("", ProductsListView.as_view(), name="product_list"),
    path("catalog/", ProductsListView.as_view(), name="product_list"),
    path("catalog/contact/", ContactListView.as_view(), name="contact"),
    path("catalog/product_detail/<int:pk>/", ProductDetailView.as_view(), name='product_detail')

]
