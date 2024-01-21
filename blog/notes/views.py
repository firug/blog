from django.shortcuts import HttpResponse, render, get_object_or_404
from django.http import Http404

from .models import Article, Partition, Chapter

def index(request):
    partitions = Partition.objects.all()
    tree = {}
    
    for part in partitions:
        tree[part] = {}
        chapters = Chapter.objects.filter(partition = part)
        for chapt in chapters:
            tree[part][chapt] = []
            articles = Article.objects.filter(chapter = chapt)
            for article in articles:
                tree[part][chapt].append(article)

    latest_articles_list = Article.objects.order_by("-pub_date")[:5]
    context = {
        "tree": tree,
        "latest_articles_list": latest_articles_list,
    }

    return render(request, "notes/index.html", context)

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        "art": article,
    }
    return render(request, "notes/detail.html", context)

def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)


def comment(request, article_id):
    return HttpResponse("You're commenting on question %s." % article_id)