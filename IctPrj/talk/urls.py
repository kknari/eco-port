from django.urls import path

from .views import talk_list

urlpatterns = [
    path('', talk_list, name='talk-list'),
]