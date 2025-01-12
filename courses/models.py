from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='courses/images/')
    video = models.FileField(upload_to='courses/videos/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exercises')
    title = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.title
