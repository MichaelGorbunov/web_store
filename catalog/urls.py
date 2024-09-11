from django.urls import include, path

# from catalog import views
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import contact

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", contact, name="contact"),
]
