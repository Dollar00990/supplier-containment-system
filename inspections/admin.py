from django.contrib import admin
from .models import InspectorRequest


@admin.register(InspectorRequest)
class InspectorRequestAdmin(admin.ModelAdmin):

    list_display = (
        "containment",
        "inspector",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )
