from django import forms


class ProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
