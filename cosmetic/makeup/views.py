from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from makeup.models import Brand, Product


# Create your views here.


def welcome_page(request):
    return render(request, "makeup/hello.html", {})


def product_list(request):
    products = Product.objects.all()
    return render(request, "../templates/makeup/products.html", {"products": products})


def brand_list(request):
    brands = Brand.objects.all()
    return render(request, "../templates/makeup/brands.html", {"brands": brands})


# class LoginView(View):
#
#     form = LoginForm
#     template_name = "makeup/user.html"
#
#     def get(self, **args):
#         context = {
#             'form' : PostForm()
#         }
#         return render(self.request, self.template_name, context)
#
#
# def post(self, **args):
#     form = self.form(self.request.POST)
#     if form


