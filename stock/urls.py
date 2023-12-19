from django.urls import path, include

from . import views

app_name = "stock"

urlpatterns = [
    path("",views.inventory, name="inventory")
]
