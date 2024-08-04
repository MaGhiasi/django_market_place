from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control form-control-lg m-2'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control m-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control m-2'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control m-2'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control m-2'
            })
        }