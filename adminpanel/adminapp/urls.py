from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Add the following line for the root path
    path('', views.login, name='login'),  # You can replace 'login' with the appropriate view name
]
