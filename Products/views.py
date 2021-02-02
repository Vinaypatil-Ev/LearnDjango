from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
# import model
from .models import ClassProducts
from .forms import ClassProductForm

def home2_view(*args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")

def home_view(request, *args, **kwargs):
    context = {
        "my_name": "my django project",
        "last_name": "mongo",
        "rnos": [1 , 2, 3, 4 , 5, "abc"],
        "my_html": "<h1> This is Html <h2>"
    }
    return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def product_details(request, *args, **kwargs):
    obj = ClassProducts.objects.all()
    form = ClassProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "Products": obj.values(),
        "form":form
    }
    return render(request, "products.html", context)

def product_details_create(request, *args, **kwargs):
    form = ClassProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form":form
    }
    return render(request, "products_create.html", context)