from django.shortcuts import render
from blog.models import Article

# Create your views here.

def article_index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'article_index.html', context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'article_detail.html', context)