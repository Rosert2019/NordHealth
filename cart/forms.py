from django import forms

"""
quantity: allows the user to select a quantity between one and 10.
override: allows you to indicate whether the quantity has to be added
to any existing quantity in the cart.
"""

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)