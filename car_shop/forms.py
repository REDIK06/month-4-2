from django import forms
from . import models


class CarShopForm(forms.ModelForm):
    class Meta:
        model = models.CarShop
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.ReviewCars
        fields = ['text']
