from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'sharespace'


urlpatterns = [
    path('', shared_view, name='main_view'),
    path('create_post', create_post, name='create_post'),
    path('<int:pk>/update', update_post, name='room_update'),
    path('<int:pk>/delete', delete_post, name='room_delete'),
    path('<int:pk>/', RoomDetail.as_view(), name='room_detail'),
]

