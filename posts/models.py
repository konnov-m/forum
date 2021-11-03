from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Role(models.Model):
    title = models.CharField(max_length=63)
    add_post = models.BooleanField()
    add_comment = models.BooleanField()
    delete_post = models.BooleanField()
    delete_comment = models.BooleanField()
    change_role = models.BooleanField()

    class Meta:
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.title


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Пользователь')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='Роль')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Профили"
