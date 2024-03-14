from django.urls import path
from . import views

urlpatterns = [
    #path('add_available_books', views.add_available_books, name='add_available_books'),
    path('add_question/', views.add_question, name='add_question'),
    path('question/', views.question, name='question')
]