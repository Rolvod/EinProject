from django.contrib import admin
from .models import Question, Quiz, Answer

admin.site.register(Question)
admin.site.register(Quiz)
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'is_correct')
    list_filter = ('is_correct', 'question__quiz')
    search_fields = ('name',)