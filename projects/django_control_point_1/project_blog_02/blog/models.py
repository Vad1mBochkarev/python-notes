from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(
        verbose_name = 'Заголовок',
        max_length = 256
    )
    text = models.TextField(
        verbose_name = 'Текст'
    )
    pub_date = models.DateTimeField(
        verbose_name = 'Дата и время публикации',
        help_text = 'Если установить дату и время в будущем — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name = 'Автор публикации'
    )
    location = models.ForeignKey(
        'Location',
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = 'Местоположение'
    )
    category = models.ForeignKey(
        'Category',
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = 'Категория'
    )
    is_published = models.BooleanField(
        verbose_name = 'Опубликовано',
        default = True
    )
    created_at = models.DateTimeField(
        verbose_name = 'Добавлено',
        auto_now_add = True
    )

    class Meta:
        verbose_name='публикация'
        verbose_name_plural = 'Публикации'

    
class Category(models.Model):
    title = models.CharField(
        verbose_name = 'Заголовок',
        max_length = 256
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    slug = models.SlugField(
        verbose_name = 'Идентификатор',
        unique = True,
        help_text = 'Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default = True,
        help_text = 'Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name = 'Добавлено',
        auto_now_add = True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField(
        verbose_name = 'Название места',
        max_length = 256
    )
    is_published = models.BooleanField(
        verbose_name = 'Опубликовано',
        default = True
    )
    created_at = models.DateTimeField(
        verbose_name = 'Добавлено',
        auto_now_add = True
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'