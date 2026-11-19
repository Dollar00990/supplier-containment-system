from django.urls import path
from .views import (
    containment_list,
    containment_create,
    containment_detail,
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

    path(
        "containments/<int:pk>/",
        containment_detail,
        name="containment_detail"
    ),
]