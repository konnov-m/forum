from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Автор')
    slug = models.SlugField()
    content = models.TextField(verbose_name='Содержимое поста')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name_plural = "Посты"

