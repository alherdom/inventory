from django.db import models

from django.urls import reverse


class Location(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_lenght=100)
    description = models.CharField(max_lenght=500)

    class Meta:
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.slug


class Product(models.Model):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=250)
    model = models.CharField(max_lenght=50)
    image = models.ImageField()

    class Meta:
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("stock:product", kwargs=dict(code=self.code))


class Item(models.Model):
    code = models.CharField(max_lenght=6, unique=True)
    serial = models.CharField(max_lenght=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.code
