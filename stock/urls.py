from django.urls import path, include

from . import views

app_name = "stock"

urlpatterns = [
    path("",views.iventory, name="inventory")
]
