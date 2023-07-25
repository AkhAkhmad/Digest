from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Subscription(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Post(models.Model):
    title = models.CharField(max_length=50)
    top = models.IntegerField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Digest(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    posts = models.ManyToManyField(Post)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Дайджест'
        verbose_name_plural = 'Дайджесты'
