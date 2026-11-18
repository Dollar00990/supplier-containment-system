from django import forms
from .models import Containment


class ContainmentForm(forms.ModelForm):

    class Meta:
        model = Containment

        fields = [
            "title",
            "supplier",
            "defect_description",
            "suspect_quantity",
            "status",
        ]