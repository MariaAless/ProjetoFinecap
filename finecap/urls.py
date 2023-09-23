from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(), name='index'),
    path('listar/', views.listReserva.as_view(), name ="listar"),
    path('criar/', views.Criar.as_view(), name ="criar"),
    path('update/<int:pk>/', views.ReservaUpdateView.as_view(), name ="update"),
    path('delete/<int:pk>/', views.Delete.as_view(), name ="delete"),
     path('detalhe/<int:pk>/', views.ReservaDetalhe.as_view(), name='detalhe'),


]