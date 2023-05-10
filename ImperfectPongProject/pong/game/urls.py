from django.urls import path
from game import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('game', views.game, name='game'),
    path('menu', views.menu, name='menu'),
    path('instructions', views.instructions, name='instructions'),
]
