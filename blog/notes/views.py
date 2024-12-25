from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

from .paginator import paginator
from .models import Article, Partition, Chapter
from .forms import ArticleWriteForm
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    articles = Article.objects.order_by('-pub_date')
    
    latest_articles_list = Article.objects.order_by("-pub_date")[:2]
    context = {
        "articles": paginator(request, articles, 8),
        "latest_articles_list": latest_articles_list,
        'user': request.user,
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

@permission_required('notes.change_article', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if (not article.authors.filter(id=request.user.id).exists()):
        return HttpResponseForbidden("Вы не являетесь автором данного поста")
    condition = (article.is_locked)
    print(condition)
    if (condition and (not article.locked_by.filter(id=request.user.id).exists())):
        return HttpResponseForbidden("Статья редактируется другим пользователем")

    article.is_locked = True
    article.locked_by.add(request.user.id)
    article.save()

    if request.method == 'POST':
        form = ArticleWriteForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            article.is_locked = False
            article.locked_by = None
            article.save()
            return redirect('notes:detail', article_id = article.id)
    else:
        initial_data = {
            'chapter' : article.chapter,
            'heading' : article.heading,
            'body': article.body,
        }
        form = ArticleWriteForm(initial=initial_data)
    return render(request, "notes/edit_article.html", {'form': form})

@permission_required('notes.add_article', raise_exception=True)
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
            article.authors.add(request.user)
            return redirect('notes:index')
    else:
        form = ArticleWriteForm()
    return render(request, 'notes/add_article.html', {'form': form})

@permission_required('notes.delete_article', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if not article.authors.filter(id=request.user.id).exists():
        return HttpResponseForbidden("Вы не можете удалить данный пост, так как вы не являетесь одним из его создателей")
    if request.method == 'POST':
        article.delete()
        return redirect('notes:index')
    
@csrf_exempt
def unlock_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.is_locked = False
    article.locked_by = None
    article.save()
    return JsonResponse({'status' : 'success'})