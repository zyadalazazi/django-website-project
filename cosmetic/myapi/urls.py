from django.urls import include, path, re_path
from rest_framework import routers
from .views import ProductList, ProductDetails, BrandList, BrandDetails
from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Cosmetic Botique API",
      default_version='v1',
      description="This is the API documentation of the Cosmetic Boutique store website API.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="testing@api.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', APIView.as_view()),
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<pk>/', ProductDetails.as_view(), name='product-detail'),
    path('brand/', BrandList.as_view(), name='brand-list'),
    path('brand/<pk>/', BrandDetails.as_view(), name='brand-detail'),
    # path('documentation', )
]