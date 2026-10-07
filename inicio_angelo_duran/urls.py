from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.index, name='index'),
    path('paisajes/', views.tema_paisajes, name='paisajes'),
    path('urbano/', views.tema_urbano, name='urbano'),
]