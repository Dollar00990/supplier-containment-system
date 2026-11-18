from django.db import models
from accounts.models import User
from containments.models import Containment


class InspectorRequest(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    )

    containment = models.ForeignKey(
        Containment,
        on_delete=models.CASCADE
    )

    inspector = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.containment} - {self.inspector}"