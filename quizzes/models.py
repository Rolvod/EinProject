from django.db import models

class Quiz(models.Model):
    name = models.CharField('Название теста', max_length=64)
    description = models.TextField('Описание', blank=True)
    photo = models.URLField('Фото (URL ссылка)', blank=True)
    public = models.BooleanField('Публична?', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Текст вопроса', max_length=255)
    photo = models.URLField('Фото (URL ссылка)', blank=True)

    def __str__(self):
        return f"{self.quiz.name} | {self.text}"
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    name = models.CharField('Вариант ответа', max_length=128)
    is_correct = models.BooleanField('Правильный ответ?', default=False)
    photo = models.URLField('Фото (URL ссылка)', blank=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f"{self.question.quiz.name} | {self.question.text} | {self.name}: {self.is_correct}"