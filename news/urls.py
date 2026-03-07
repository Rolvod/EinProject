from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name='news'),
    path('<int:id>/', views.current_news, name='current_news')
]