from django.urls import path

from .views import (
    containment_list,
    containment_create
)

urlpatterns = [

    path(
        "containments/",
        containment_list,
        name="containment_list"
    ),

    path(
        "containments/new/",
        containment_create,
        name="containment_create"
    ),

]