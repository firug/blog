from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from notes.models import Article
from users.models import Comment

# Получаем ContentType для модели Article
content_type = ContentType.objects.get_for_model(Article)

# Создаём разрешения
add_article = Permission.objects.get(codename='add_article', content_type=content_type)
change_article = Permission.objects.get(codename='change_article', content_type=content_type)
delete_article = Permission.objects.get(codename='delete_article', content_type=content_type)
view_article = Permission.objects.get(codename='view_article', content_type=content_type)

comment_content_type = ContentType.objects.get_for_model(Comment)
comment_article = Permission.objects.get(codename='add_comment',content_type=comment_content_type)

# Создаём группы
authors, created = Group.objects.get_or_create(name='Авторы')
readers, created = Group.objects.get_or_create(name='Читатели')

# Назначаем разрешения группам
authors.permissions.set([add_article, change_article, view_article, comment_article])
readers.permissions.set([view_article, comment_article])