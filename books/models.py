from django.db import models

# Create your models here.
class available_books(models.Model):
    
    Course_title=models.CharField(max_length=250)
    books_name=models.CharField(max_length=250)
    owner_name=models.CharField( max_length=250)
    writer_name=models.CharField(max_length=250)
    roll=models.CharField(max_length=250)
    session=models.CharField(max_length=250)

class need_books(models.Model):
    Course_title=models.CharField(max_length=250, default="cse")
    books_name=models.CharField(max_length=250, default="hall")
    borrower_name=models.CharField(max_length=250)
    writer_name=models.CharField(max_length=250)
    roll=models.CharField(max_length=250)
    session=models.CharField(max_length=250)
    