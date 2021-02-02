from Products.views import contact_view, home2_view, home_view, product_details, product_details_create
from django.urls import path


urlpatterns = [
    path("", home_view, name="HOME"),
    path("home2/", home2_view),
    path("contact", contact_view),
    path("products/", product_details),
    path("products/create", product_details_create),
    
]