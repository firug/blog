from django.contrib import admin

from .models import Partition, Chapter, Article

admin.site.register(Partition)
admin.site.register(Chapter)
admin.site.register(Article)