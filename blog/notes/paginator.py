from django.core.paginator import Paginator

def paginator(request, articles, articles_on_the_page):
    paginator = Paginator(articles, articles_on_the_page)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)