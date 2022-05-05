from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='Название поста', max_length=160, unique=True)
    description = models.TextField(verbose_name='Краткое описание', blank=True)
    image = models.ImageField(verbose_name='Основная фотография', upload_to='images/posts/', null=True)
    content = models.TextField(verbose_name='Содержание поста')
    category = models.ForeignKey(to='category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(to='tag', verbose_name='Теги', related_name='post_tags', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, blank=True)
    created_by = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, related_name='author')
    update_by = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, related_name='reditor', blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=60)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    title = models.CharField(verbose_name='Название тега', max_length=60)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(models.Model):
    content = models.TextField(verbose_name='Сообщение', max_length=500)
    post = models.ForeignKey(to='post', verbose_name='ID поста', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    created_by = models.ForeignKey(to='auth.user', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Reply(models.Model):
    content = models.TextField(verbose_name='Сообщение', max_length=500)
    comment  = models.ForeignKey(to='comment', verbose_name='ID комментария', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    created_by = models.ForeignKey(to='auth.user', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Like(models.Model):
    user = models.ForeignKey(to='auth.user', verbose_name='ID пользователя', on_delete=models.CASCADE)
    post = models.ForeignKey(to='post', verbose_name='ID поста', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class View(models.Model):
    user = models.ForeignKey(to='auth.user', verbose_name='ID пользователя', on_delete=models.CASCADE)
    post = models.ForeignKey(to='post', verbose_name='ID поста', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Просмотр  поста'
        verbose_name_plural = 'Просмотры постов'

