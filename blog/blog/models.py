from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(u'Заголовок', max_length=255)
    text = models.TextField(u'Текст')
    date = models.DateTimeField(u'Дата создания')
    hidden = models.BooleanField(u'Скрытый пост', default=False)

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def get_absolute_url(self):
        return f'/post/{self.pk}'

    def __str__(self):
        return f'{self.pk} | {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(u'Текст')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return '{} | {}'.format(self.pk, self.text)
    