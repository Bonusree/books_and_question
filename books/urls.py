from django.urls import path
from . import views

urlpatterns = [
    path('add_available_books', views.add_available_books, name='add_available_books'),
    path('add_need_books', views.add_need_books, name='add_need_books'),
    
]