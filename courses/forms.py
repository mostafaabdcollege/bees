from django import forms
from .models import Course, Exercise

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'date', 'duration', 'price', 'image', 'video', 'active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Par exemple : 2024-10-10'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de heure par cours'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image de Cours'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'placeholder':'Védio de Cours'}),
            'active': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        
        fields = ['course', 'title', 'option1', 'option2', 'option3', 'option4', 'correct_answer']
        
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'question'}),
            'option1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'option1'}),
            'option2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'option2'}),
            'option3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'option3'}),
            'option4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'option4'}),
            'correct_answer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'option corréct'}),
        }