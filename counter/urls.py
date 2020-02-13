from django.urls import path

from . import views

urlpatterns = [
    path('plus/', views.plus, name='plus'),
    path('', views.index, name='index'),
]