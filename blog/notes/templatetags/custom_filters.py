from django import template
from django.utils.safestring import mark_safe

from bs4 import BeautifulSoup
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter
def bleach_clean(value):
    soup = BeautifulSoup(value, 'html.parser')
    return soup.get_text()
