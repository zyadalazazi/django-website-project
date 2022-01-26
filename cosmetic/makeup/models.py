from django.db import models

# Create your models here.


class Brand:
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)

    def __str__(self):
        pass

    def get_absolute_url(self):
        pass


class Product:
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    description = models.TextField()
    expire_date = models.DateField()
    price = models.FloatField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

