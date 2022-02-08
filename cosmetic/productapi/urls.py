from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

# router_brand = routers.DefaultRouter()
# router_brand.register(r'brand', views.BrandViewSet)

urlpatterns = [
    # path('', include(router_product.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]