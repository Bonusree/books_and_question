from django.db import models
from books.models import course_title
# Create your models here.
class Question_bank(models.Model):
    session =models.CharField(max_length=100,null=True)
    Exam_type=models.CharField(max_length=240,null=True)
    faculty=models.CharField(max_length=100,null=True)
    Course_title=models.ForeignKey(course_title, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')
    