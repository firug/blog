from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Chapter, Article
from tinymce.widgets import TinyMCE

class MyForm(forms.Form):
    myfield = MarkdownxFormField()

class ArticleWriteForm(forms.Form):
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all())
    heading = forms.CharField(max_length=200, required=True)
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    image = forms.ImageField(
                widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}), required=False
    )

    class Meta:
        model = Article
        fields = ('chapter', 'heading', 'body', 'image')