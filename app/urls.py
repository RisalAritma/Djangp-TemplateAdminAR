from django.urls import path
from . import views, views_fakultas

app_name = 'app'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),


    # FAKULTAS
    path('dashboard_fakultas/', views_fakultas.dashboard, name='dashboard_fakultas'),


]

