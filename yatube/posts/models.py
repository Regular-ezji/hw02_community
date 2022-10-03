from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    class Meta:
        ordering = ['-pub_date']

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )


class Group(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
