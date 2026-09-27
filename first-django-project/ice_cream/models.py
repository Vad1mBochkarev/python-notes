from django.db import models
from core.models import PublishModel


class Wrapper(PublishModel):
    title = models.CharField(max_length=256)


class Topping(PublishModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


class Category(PublishModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.IntegerField(default=100)


class IceCream(PublishModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)

    wrapper = models.OneToOneField(Wrapper, on_delete=models.SET_NULL, null=True, related_name='ice_cream')
    toppings = models.ManyToManyField(Topping, related_name='ice_cream')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ice_creams')
    