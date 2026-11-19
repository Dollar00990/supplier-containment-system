from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import InspectorRequest


@login_required
def my_assignments(request):

    assignments = InspectorRequest.objects.filter(
        inspector=request.user
    ).order_by("-created_at")

    return render(
        request,
        "inspections/my_assignments.html",
        {
            "assignments": assignments
        }
    )

@login_required
def accept_assignment(request, pk):

    assignment = get_object_or_404(
        InspectorRequest,
        pk=pk
    )

    assignment.status = "accepted"
    assignment.save()

    return redirect("my_assignments")


@login_required
def decline_assignment(request, pk):

    assignment = get_object_or_404(
        InspectorRequest,
        pk=pk
    )

    assignment.status = "declined"
    assignment.save()

    return redirect("my_assignments")