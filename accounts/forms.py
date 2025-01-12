from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser,Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_teacher', 'is_student']
# profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'level','user_type','bio']