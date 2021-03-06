"""cosmetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from makeup.views import (brand_list, base, index, shop, ProductDetailView,
                          register, log_in, log_out, password_reset_request,
                          ProductCreateView, ProductUpdateView, ProductDeleteView)
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

admin.site.site_header = "Cosmetic Boutique Admin Page"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Cosmetic Boutique Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', brand_list, name="brands"),
    path('base/', base),
    path('', index, name="index"),
    path('shop/', shop, name="shop"),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('register/', register, name="register"),
    path('login/', log_in, name="log_in"),
    path('logout/', log_out, name="log_out"),
    path('create-product/', ProductCreateView.as_view(template_name='makeup/product-create.html'), name="create-product"),
    path('update/<int:pk>', ProductUpdateView.as_view(template_name='makeup/product-update.html'), name="update-product"),
    path('delete/<int:pk>', ProductDeleteView.as_view(template_name='makeup/product-delete.html'), name="delete-product"),
    path('api/', include('myapi.urls'), name='api'),
    # path('password_reset/', password_reset_request, name="password_reset"),
    # path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
