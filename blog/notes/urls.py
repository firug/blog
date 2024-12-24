from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
	path('', views.index, name='index'),
	path("<int:article_id>/", views.detail, name="detail"),
	path("<int:article_id>/results/", views.results, name="results"),
    path("<int:article_id>/comment/", views.comment, name="comment"),
	path("add_article", views.add_article, name='add_article'),
    path("edit_article/<int:article_id>", views.edit_article, name='edit_article'),
	path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),
]