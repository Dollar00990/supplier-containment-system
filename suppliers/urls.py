from django.urls import path
from .views import supplier_list, supplier_create

urlpatterns = [
    path(
        "suppliers/",
        supplier_list,
        name="supplier_list"
    ),

    path(
        "suppliers/new/",
        supplier_create,
        name="supplier_create"
    ),
]