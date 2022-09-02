from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name='home'),
    path("login/",views.loginSystem, name='login'),
    path("room/<str:pk>/",views.room, name='room'),
    path("create-room/",views.createRoom, name='room_form'),
    path("update-room/<str:pk>",views.updateRoom, name='update_room'),
    path("delete-room/<str:pk>",views.deleteRoom, name='delete_room'),
]
