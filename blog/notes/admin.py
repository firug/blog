from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Partition, Chapter, Article, Post

class AdminPostModel:
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Partition)
admin.site.register(Chapter)
admin.site.register(Article)
#admin.site.register(AdminPostModel)