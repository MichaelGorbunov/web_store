from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import contact,send

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/home/", views.home, name="home"),
    path("catalog/contact/", contact, name="contact"),
    path("catalog/send/", send, name="send"),
]
