from django.db import models
from markdownx.models import MarkdownxField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Partition(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

class Chapter(models.Model):
    partition = models.ForeignKey(Partition, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class Article(models.Model):
    chapter = models.ForeignKey(Chapter, models.SET_NULL, blank=True, null=True)
    heading = models.CharField(max_length=200)
    body = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='articles/',
        blank=True,
    )
    authors = models.ManyToManyField(User, related_name='articles')

    def __str__(self) -> str:
        return str(self.heading)
