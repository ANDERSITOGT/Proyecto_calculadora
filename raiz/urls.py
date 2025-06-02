from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_raiz, name='calculadora'),
    path('resultado/', views.ver_resultado, name='ver_resultado'),

]
