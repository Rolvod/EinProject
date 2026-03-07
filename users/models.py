from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description = models.TextField('Описание', blank=True)
    nickname = models.CharField('Никнейм', blank=True)
    profile_picture = models.URLField('Фото профиля', default='https://www.shareicon.net/data/128x128/2015/09/24/106422_user_512x512.png', max_length=512)
    points = models.IntegerField('Баллы', default=0)
    completed_quizzes = models.JSONField('Пройденные тесты', default=dict, blank=True)

    def __str__(self):
        return self.username
    
    def rank(self):
        if self.points >= 500:
            return 'Полковник'
        elif self.points >= 450:
            return 'Подполковник'
        elif self.points >= 400:
            return 'Майор'
        elif self.points >= 350:
            return 'Капитан'
        elif self.points >= 250:
            return 'Прапорщик'
        elif self.points >= 200:
            return 'Старшина'
        elif self.points >= 150:
            return 'Сержант'
        elif self.points >= 100:
            return 'Ефрейтор'
        elif self.points >= 50:
            return 'Рядовой'
        else:
            return 'Новобранец'

        
    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'