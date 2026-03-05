from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_profile, name='current_profile'),
    path('change_profile', views.change_profile, name='change_profile'),
    path('<str:username>/', views.profile, name='profile')
]