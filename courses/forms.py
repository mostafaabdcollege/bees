from django import forms
from .models import Course, Exercise

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'date', 'duration', 'price', 'image', 'video', 'active']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['course', 'title', 'option1', 'option2', 'option3', 'option4', 'correct_answer']
