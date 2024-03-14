from django.db import models
from books.models import course_title
# Create your models here.

class Course(models.Model):
    Course_title=models.ForeignKey(course_title, on_delete=models.CASCADE)
    sessions = models.ForeignKey('Session', on_delete=models.CASCADE)
    exam_type=models.CharField(max_length=100)

class Session(models.Model):
    faculty = models.CharField(max_length=250)
    date = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
