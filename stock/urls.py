from django.urls import path, include

from . import views

app_name = "stock"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<str:code>/", views.product_detail, name="product_detail"),
    path("search/", views.search, name="search"),
]
