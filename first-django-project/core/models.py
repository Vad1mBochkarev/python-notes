from django.db import models

# Create your models here.
class PublishModel(models.Model):
    is_published = models.BooleanField('Публикация', default=True)

    class Meta:
        abstract = True
        verbose_name = 'публикация'        
        verbose_name_plural = 'публикации'
