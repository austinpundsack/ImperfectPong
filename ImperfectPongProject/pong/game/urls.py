from django.urls import path
from game import views

urlpatterns = [
    path('', views.instructions, name='instructions'),
]