from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import contact,send

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.products_list, name="product_list"),
    path("catalog/", views.products_list, name="product_list"),
    path("catalog/contact/", contact, name="contact"),
    path("catalog/send/", send, name="send"),
    path("catalog/product_detail/<int:product_id>/", views.product_detail, name="product_detail"),

]
