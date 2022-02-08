# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework import status


from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import render
from makeup.models import Brand, Product
from .serializer import BrandSerializer, ProductSerializer

# Create your views here.


class ProductList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer
    permission_classes = ['AllowAny']

    def get(self, request, *args, **kwargs):
        """
        This is a list of all the available products
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        This is used to enter a new product to the list of products
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.create(request, *args, **kwargs)


class ProductDetails(generics.GenericAPIView,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        """
        This is used to view a certain product from the available products
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        This is used to update the information of a certain product in the list
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        This is used to remove a certain product from the existing list
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.destroy(request, *args, **kwargs)


class BrandList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Brand.objects.all().order_by('pk')
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        """
        This is a list of all the available brands
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        This is used to enter a new product to the list of brands
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.create(request, *args, **kwargs)


class BrandDetails(generics.GenericAPIView,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    # lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        """
        This is used to view a certain brand from the available products
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        This is used to update the information of a certain brand in the list
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        This is used to remove a certain brand from the existing list
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.destroy(request, *args, **kwargs)

