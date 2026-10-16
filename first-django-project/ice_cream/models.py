from django.db import models
from core.models import PublishModel


class Wrapper(PublishModel):
    title = models.CharField('название', max_length=256)

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'обёртки'

    def __str__(self):
        return self.title


class Topping(PublishModel):
    title = models.CharField('название', max_length=256)
    slug = models.SlugField('слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'начинка'
        verbose_name_plural = 'начинки'

    def __str__(self):
        return self.title


class Category(PublishModel):
    title = models.CharField('название', max_length=256)
    slug = models.SlugField('слаг', max_length=64, unique=True)
    output_order = models.IntegerField('порядок вывода', default=100)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class IceCream(PublishModel):
    title = models.CharField('название', max_length=256)
    description = models.TextField('описание')
    is_on_main = models.BooleanField('на главной', default=False)

    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ice_cream',
        verbose_name='обёртка',
    )
    toppings = models.ManyToManyField(
        Topping,
        related_name='ice_cream',
        verbose_name='начинки',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='категория',
    )

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return self.title
