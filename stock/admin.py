from django.contrib import admin

from .models import Product, Item, Location


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "description", "brand", "model", "image")
    list_editable = ("code", "name", "description", "brand", "model", "image")
    list_filter = ("brand", "model")
    search_fields = ("code", "name", "description")
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "serial")
    list_editable = ("code", "serial")
    list_filter = ("product", "location")
    search_fields = ("code", "serial")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description")
    list_editable = ("name", "slug", "description")
    list_filter = ("name",)
    search_fields = ("name", "description")
    prepopulated_fields = dict(slug=("name",))
