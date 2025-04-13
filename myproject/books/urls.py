from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.book_add, name='book_add'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('registration/logout/', views.user_logout, name='logout'),
]