from django.shortcuts import render
from django.http import HttpResponse
from makeup.models import Brand, Product

# Create your views here.


def welcome_page(request):

    return render(request, "makeup/hello.html", {})
