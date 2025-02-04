from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        
        model = Product
        
        fields = ['name', 'price', 'stock', 'image', 'description']

        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de produit'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix de produit'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image de Produit'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }