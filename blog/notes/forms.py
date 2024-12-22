from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Chapter, Article

class MyForm(forms.Form):
    myfield = MarkdownxFormField()

class ArticleWriteForm(forms.Form):
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all())
    heading = forms.CharField(max_length=200, required=True)
    body = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40,
                                     'class': 'resizable-textarea'})
    )
    image = forms.ImageField(
                widget=forms.ClearableFileInput(attrs={'accept': 'image/*'})
    )

    class Meta:
        model = Article
        fields = ('chapter', 'heading', 'body', 'image')