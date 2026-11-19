from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inspections.models import InspectorRequest

from .models import Containment
from .forms import ContainmentForm


@login_required
def containment_list(request):

    containments = Containment.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "containments/list.html",
        {
            "containments": containments
        }
    )


@login_required
def containment_create(request):

    if request.method == "POST":

        form = ContainmentForm(request.POST)

        if form.is_valid():

            containment = form.save(commit=False)

            containment.created_by = request.user

            containment.save()

            return redirect("containment_list")

    else:

        form = ContainmentForm()

    return render(
        request,
        "containments/create.html",
        {
            "form": form
        }
    )
@login_required
def containment_detail(request, pk):

    containment = get_object_or_404(
        Containment,
        pk=pk
    )

    inspector_requests = InspectorRequest.objects.filter(
        containment=containment
    )

    return render(
        request,
        "containments/detail.html",
        {
            "containment": containment,
            "inspector_requests": inspector_requests,
        }
    )