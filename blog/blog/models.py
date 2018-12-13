from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(u'Заголовок', max_length=255)
    text = models.TextField(u'Текст')
    date = models.DateTimeField(u'Дата создания', auto_now_add=True)
    hidden = models.BooleanField(u'Скрытый пост', default=False)
    views = models.PositiveIntegerField(u'Просмотры', default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return '/post/{}'.format(self.pk)

    def __str__(self):
        return '{} | {}'.format(self.pk, self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(u'Текст')
    date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return '{} | {}'.format(self.pk, self.text)
