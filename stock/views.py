from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from .models import Product, Item, Location


def inventory(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    items = Item.objects.select_related("product", "location").all()
    paginator = Paginator(items, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "inventory.html",
        dict(products=products, items=items, page_obj=page_obj),
    )


def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    product = Product.objects.get(pk=pk)
    items = Item.objects.filter(product=product)
    return render(request, "product_detail.html", dict(product=product, items=items))


def location_detail(request: HttpRequest, pk: int) -> HttpResponse:
    location = Location.objects.get(pk=pk)
    items = Item.objects.filter(location=location)
    return render(request, "location_detail.html", dict(location=location, items=items))


def item_detail(request: HttpRequest, pk: int) -> HttpResponse:
    item = Item.objects.get(pk=pk)
    return render(request, "item_detail.html", dict(item=item))


def search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("query")
    items = Item.objects.filter(product__name__icontains=query)
    return render(request, "search.html", dict(items=items, query=query))
