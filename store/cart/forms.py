from statistics import quantiles
from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(max_value=100, min_value=1)
