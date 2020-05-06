from .views import book_list, photo_create, photo_delete

from django.contrib import admin
from django.urls import path


app_name = "viewspace"


urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/', photo_create, name='book_create'),
    path('<int:pk>/delete/', photo_delete, name='book_delete'),
]
