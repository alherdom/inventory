from django.contrib import admin

from .models import Product, Item, Location


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "description", "brand", "model", "image")
    list_editable = ("code", "name", "description", "brand", "model", "image")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "serial")
    list_editable = ("code", "serial")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description")
    list_editable = ("name", "slug", "description")
    prepopulated_fields = dict(slug=("name",))
