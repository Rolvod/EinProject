from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes_page, name='quizzes'),
    path('<int:id>', views.quiz_detail, name='current_quiz')
]