from django.shortcuts import render
from blog.models import Article, Category, Comment
from blog.forms.CommentForm import CommentForm

# Create your views here.

def article_index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'article_index.html', context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                article=article
            )
            comment.save()

    context = {
        'article': article,
        'comments': comments,
        'form': form
    }
    return render(request, 'article_detail.html', context)

def category_index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_index.html', context)
    
def article_by_category_index(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    articles = Article.objects.filter(category=category)
    context = {
        'articles': articles,
        'category_name': category.name
    }
    return render(request, 'article_index.html', context)