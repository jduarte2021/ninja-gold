from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process-money', views.money),
    path('limpiar',views.limpiar),
]
