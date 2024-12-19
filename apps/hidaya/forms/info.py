from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.hidaya.models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
