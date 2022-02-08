from rest_framework import serializers
from makeup.models import Brand, Product


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', 'origin')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'kind', 'description', 'expire_date', 'price', 'brand')
