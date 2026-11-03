from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField(
        'Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        help_text='Рекомендованная розничная цена',
    )
    comment = models.TextField('Комментарий', blank=True)
