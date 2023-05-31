from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('books/', views.books, name='books'),
    path('question/', views.question, name='question'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.LogoutPage, name='logout')
]