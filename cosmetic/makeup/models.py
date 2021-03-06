from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name_plural = "Featured Brands"


class Product(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    description = models.TextField()
    expire_date = models.DateField()
    price = models.FloatField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return "The name is {0}, its price is {1} and its brand is {2}".format(self.name, self.price, self.brand)

    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id])

    class Meta:
        verbose_name_plural = "Available Products"


# class PostUser(User):
#     mobile_number


