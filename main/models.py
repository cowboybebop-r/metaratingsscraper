from django.db import models


class Feedback(models.Model):
    username = models.CharField("Имя пользователя", max_length=255, null=True)
    source = models.CharField("Источник", max_length=255, null=True)
    content = models.TextField("Содержание")
    post_date = models.DateField("Дата публикации", null=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ['post_date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
