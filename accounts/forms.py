from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser,Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'})
    )
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'is_teacher', 'is_student']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prénom'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'profile_picture'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez le mot de passe'}),
            'is_teacher': forms.NullBooleanSelect(attrs={'class': 'form-control'}), 
            'is_student': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bio'}),
            
        }
        
# profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'level','user_type','bio']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile picture'}),
            'level': forms.Select(attrs={'class': 'form-control'}), 
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'biographie'}),
        }