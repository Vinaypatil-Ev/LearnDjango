from Products.views import contact_view, home2_view, home_view, product_details, product_details_by_id, product_details_create, product_details_create_by_raw, product_details_delete
from django.urls import path


urlpatterns = [
    path("", home_view, name="HOME"),
    path("home2/", home2_view),
    path("contact", contact_view),
    path("products/", product_details, name="products"),
    path("products/create", product_details_create),
    path("products/create/raw", product_details_create_by_raw, name="raw"),
    path("products/<int:id>", product_details_by_id, name="product_by_id"),
    path("products/delete", product_details_delete, name="product_delete"),
    
]