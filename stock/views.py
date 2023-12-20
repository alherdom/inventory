from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .utils import code_generator
from django.core.paginator import Paginator
from .models import Product, Item, Location


def inventory(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    items = Item.objects.select_related("product", "location").all()
    return render(request, "inventory.html", dict(products=products, items=items))
