from django.db import models


class Post(models.Model):
    """Post model."""

    title = models.CharField(
        max_length=40,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='изображение',
        blank=True
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    
    def __str__(self):
        return self.title