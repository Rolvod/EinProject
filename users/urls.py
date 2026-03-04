from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.ulogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.ulogout, name='logout')
]