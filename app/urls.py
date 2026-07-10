from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alert/', views.alert, name='alert'),
    path('button/', views.button, name='button'),



]

