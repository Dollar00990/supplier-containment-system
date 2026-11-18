from django.db import models
from suppliers.models import Supplier
from accounts.models import User


class Containment(models.Model):

    STATUS_CHOICES = (
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
    )

    title = models.CharField(
        max_length=200
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    defect_description = models.TextField()

    suspect_quantity = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
