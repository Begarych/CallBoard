from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    TYPE = [
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('DD', 'ДД'),
        ('traders', 'Торговцы'),
        ('gildemasters', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=12, choices=TYPE, default='tank')
    ad_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='Загаловок')
    text = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} : {self.title}'

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    response_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='Ваш отклик')
    ad = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author}: {self.text}'

    def get_absolute_url(self):
        return reverse('response')
