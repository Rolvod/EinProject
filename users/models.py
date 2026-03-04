from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description = models.TextField('Описание', blank=True)
    profile_picture = models.URLField('Фото профиля', default='https://www.shareicon.net/data/128x128/2015/09/24/106422_user_512x512.png', max_length=512)
    points = models.IntegerField('Баллы', default=0)
    completed_quizzes = models.JSONField('Пройденные тесты', default=dict, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'