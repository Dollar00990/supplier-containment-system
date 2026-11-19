from django.urls import path

from .views import (
    my_assignments,
    accept_assignment,
    decline_assignment
)

urlpatterns = [

    path(
        "my-assignments/",
        my_assignments,
        name="my_assignments"
    ),
    path(
        "assignment/<int:pk>/accept/",
        accept_assignment,
        name="accept_assignment"
    ),

    path(
        "assignment/<int:pk>/decline/",
        decline_assignment,
        name="decline_assignment"
    ),


]