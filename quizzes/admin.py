from django.contrib import admin
from .models import Quiz, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
