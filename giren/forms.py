from django import forms
from giren.models import giren


class GirenForm(forms.ModelForm):
    san = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = giren
        fields = "__all__"
