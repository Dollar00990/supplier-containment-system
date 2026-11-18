
from django.contrib import admin
from .models import Containment


@admin.register(Containment)
class ContainmentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "supplier",
        "status",
        "suspect_quantity",
        "created_at",
    )

    list_filter = (
        "status",
        "supplier",
    )