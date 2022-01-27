from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome_page(request):

    return render(request, "makeup/hello.html", {})
