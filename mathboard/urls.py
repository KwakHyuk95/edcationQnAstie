from django.urls import path
from .import views

app_name='mathboard'

urlpatterns = [
    path('', views.index),
]
