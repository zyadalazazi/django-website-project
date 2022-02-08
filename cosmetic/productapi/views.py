from rest_framework import viewsets

from .serializer import ProductSerializer
from makeup.models import Brand, Product
from django.shortcuts import render

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer



