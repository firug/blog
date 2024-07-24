from .models import Partition, Chapter, Article 

from django.db import models
from django.contrib import admin

from markdownx.widgets import AdminMarkdownxWidget


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(Partition)
admin.site.register(Chapter)
admin.site.register(Article, MyModelAdmin)
#admin.site.register(AdminPostModel)