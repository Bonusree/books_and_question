from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class course_title(models.Model):
    Course_title=models.CharField(max_length=250)
    
class available_books(models.Model):
    
    Course_title=models.ForeignKey(course_title, on_delete=models.CASCADE)
    books_name=models.CharField(max_length=250)
    owner_name=models.CharField( max_length=250)
    writer_name=models.CharField(max_length=250)
    roll=models.CharField(max_length=250)
    session=models.CharField(max_length=250)
    
class need_books(models.Model):
    Course_title=models.ForeignKey(course_title, on_delete=models.CASCADE)
    books_name=models.CharField(max_length=250, default="hall")
    borrower_name=models.CharField(max_length=250)
    writer_name=models.CharField(max_length=250)
    roll=models.CharField(max_length=250)
    session=models.CharField(max_length=250)

from django.db import models
from django.conf import settings


class beg_for_book(models.Model):
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ForeignKey(available_books, on_delete=models.CASCADE)
