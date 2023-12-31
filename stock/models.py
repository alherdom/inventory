from django.db import models
from django.urls import reverse
from .utils import code_generator

CODE_LENGTH = 6


class Product(models.Model):
    code = models.CharField(max_length=6, unique=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=50)
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.code:
            code = code_generator(CODE_LENGTH)
            codes = Product.objects.values_list("code", flat=True)
            while code in codes:
                code = code_generator(CODE_LENGTH)
            self.code = code
        return super(Product, self).save(*args, **kwargs)



class Location(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.slug


class Item(models.Model):
    code = models.CharField(max_length=6, unique=True, blank=True)
    serial = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="location"
    )

    def save(self, *args, **kwargs) -> None:
        if not self.code:
            code = code_generator(CODE_LENGTH)
            codes = Item.objects.values_list("code", flat=True)
            while code in codes:
                code = code_generator(CODE_LENGTH)
            self.code = code
        return super(Item, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.code

    def get_absolute_url(self):
        return reverse("stock:product_detail", kwargs=dict(code=self.product.code))