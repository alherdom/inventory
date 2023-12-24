from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from .models import Product, Item, Location
from django.db.models import Q


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    items = Item.objects.select_related("product", "location").all()
    paginator = Paginator(items, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "product_list.html",
        dict(products=products, items=items, page_obj=page_obj),
    )


def product_detail(request: HttpRequest, code: str) -> HttpResponse:
    # product = Product.objects.get(code=code)
    product = get_object_or_404(Product, code=code)
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
    query = request.GET.get("input", "")
    print("Query:", query)
    # items = Item.objects.select_related("product", "location").filter(product__name__icontains=query)
    products = Product.objects.filter(name__icontains=query)
    # print("SQL Query:", str(items.query))
    return render(request, "search.html", dict(products=products, query=query))