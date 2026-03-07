from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')
    photo = models.URLField('Фото (URL ссылка)', blank=True)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-date',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'