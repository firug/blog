from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.http import Http404

from .paginator import paginator
from .models import Article, Partition, Chapter
from .forms import ArticleWriteForm

def index(request):
    articles = Article.objects.order_by('-pub_date')
    
    latest_articles_list = Article.objects.order_by("-pub_date")[:2]
    context = {
        "articles": paginator(request, articles, 8),
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

def add_article(request):
    if request.method == 'POST':
        form = ArticleWriteForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article(
                chapter = form.cleaned_data['chapter'],
                heading = form.cleaned_data['heading'],
                body = form.cleaned_data['body'],
                image = form.cleaned_data['image'],
            )
            article.save()
            return redirect('notes:home')
    else:
        form = ArticleWriteForm()
    return render(request, 'notes/add_article.html', {'form': form})
