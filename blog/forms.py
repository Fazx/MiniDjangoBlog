from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #继承Django表单类
    class Meta:
        model = Article
        fields = {'title','body'}