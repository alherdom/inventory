from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .utils import code_generator
from django.core.paginator import Paginator
from .models import Product, Item, Location


def check_code(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, "index.html", dict(products=products))
