from django.contrib import admin

# Register your models here.
from users.models import CustomUser


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    pass
