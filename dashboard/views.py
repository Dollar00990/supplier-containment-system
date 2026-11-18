from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from suppliers.models import Supplier
from containments.models import Containment
from inspections.models import InspectorRequest


@login_required
def dashboard(request):

    context = {
        "supplier_count":
            Supplier.objects.count(),

        "containment_count":
            Containment.objects.count(),

        "open_containments":
            Containment.objects.filter(
                status="open"
            ).count(),

        "pending_requests":
            InspectorRequest.objects.filter(
                status="pending"
            ).count(),
    }

    return render(
        request,
        "dashboard/index.html",
        context
    )