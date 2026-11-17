from django.db import models


class Supplier(models.Model):
    supplier_code = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=200
    )

    contact_person = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.supplier_code} - {self.name}"