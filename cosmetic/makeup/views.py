from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from makeup.models import Brand, Product
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NewUserForm, ProductCreateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.


def welcome_page(request):
    return render(request, "makeup/hello.html", {})


def brand_list(request):
    brands = Brand.objects.all()
    return render(request, "../templates/makeup/brands.html", {"brands": brands})


def base(request):
    return render(request, "../templates/makeup/base.html", {})


def index(request):
    first_products = Product.objects.all()[0:6]
    latest_products = list(Product.objects.all())[-4:]
    context = {'first_products': first_products, 'latest_products': latest_products}
    return render(request, "../templates/makeup/index.html", context)


def shop(request):
    products = Product.objects.all()
    return render(request, "../templates/makeup/shop.html", {'products': products})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "../templates/makeup/register.html", {'register_form': NewUserForm})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "makeup/login.html", {"login_form": form})


def log_out(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="makeup/password/password_reset.html", context={"password_reset_form":password_reset_form})


class ProductDetailView(DetailView):
    template_name = 'makeup/detail.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'makeup/product-create.html'
    success_url = '/create-product'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'makeup/product-update.html'
    success_url = '/'


class ProductDeleteView(DeleteView):
    template_name = 'makeup/product-delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy("shop")





