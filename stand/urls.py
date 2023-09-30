from django.urls import path
from . import views
app_name = "stand"
urlpatterns = [
 
    path('listarStand/', views.listStand.as_view(), name ="listarStand"),
    path('criarStand/', views.CriarStand.as_view(), name ="criarStand"),
    path('updateStand/<int:pk>/', views.StandUpdateView.as_view(), name ="updateStand"),
    path('deleteStand/<int:pk>/', views.Delete.as_view(), name ="deleteStand"),
     path('detalheStand/<int:pk>/', views.StandDetalhe.as_view(), name='detalheStand'),


]