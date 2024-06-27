from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>/', views.sensor_detail, name='sensor_detail'),
    path('<str:id>/export/', views.export_sensor_data_csv, name='export_sensor_data_csv'),
]
