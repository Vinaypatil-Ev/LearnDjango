from django.db.models.query import RawQuerySet
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
# import model
from .models import ClassProducts
from .forms import ClassProductForm, RawProductForm

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
    form = ClassProductForm()
    context = {
        "Products": obj.values(),
        "form":form
    }
    if request.method == "POST":
        form = ClassProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "products.html", context)
    elif request.method == "GET":
        return render(request, "products.html", context)

def product_details_create(request, *args, **kwargs):
    form = ClassProductForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = ClassProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "products_create.html", context)
    elif request.method == "GET":
        return render(request, "products_create.html", context)

def product_details_create_by_raw(request):
    form = RawProductForm()  
    context = {
        "form": form
    }
    if request.method == "POST":
        form = ClassProductForm(request.POST or None)
        if form.is_valid():
            print("raw product saved")
            form.save()
        return render(request, "form.html", context)
    elif request.method == "GET":
        return render(request, "form.html", context)
    
    
def product_details_by_id(request, id):
    # data = ClassProducts.objects.get(id=id)
    # data = get_object_or_404(ClassProducts, id=id)
    try:
        data = get_object_or_404(ClassProducts, id=id)
    except ClassProducts.DoesNotExist:
        raise Http404
    context = {
        "prod": data
    }
    return render(request, "dynamic.html", context)

def product_details_delete(request):
    data = ClassProducts.objects.all()
    context = {
        "Products":data.values(),
    }
    if request.method == "POST":
        print("post method")
        print(request.POST["id"])
        product = ClassProducts.objects.get(id=request.POST["id"])
        product.delete()
    return render(request, "product_delete.html", context)