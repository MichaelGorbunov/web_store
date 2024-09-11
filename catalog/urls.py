from django.urls import include, path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
]