from django.contrib import admin
from books.models import *

admin.site.register(course_title)
admin.site.register(available_books)
admin.site.register(need_books)

