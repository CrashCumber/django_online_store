from django import forms


class ProductForm(forms.Form):
    number = forms.IntegerField(min_value=1)

