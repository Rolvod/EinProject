from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_profile, name='current_profile'),
    path('<string:username>', views.profile, name='profile')
]