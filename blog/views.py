from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from blog.models import Article, Category, Comment
from blog.forms.CommentForm import CommentForm

# Create your views here.

class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by('-created_on')
        context = {
            'articles': articles
        }
        return render(request, 'article_index.html', context)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['author', 'body']

    def form_valid(self, form):
        article = Article.objects.get(id=self.kwargs['pk'])
        Comment.objects.create(
            article=article,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("article_detail", kwargs={"pk": self.kwargs['pk']}))


class ArticleDetailsView(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(article=article)
        form = CommentForm()

        context = {
            'article': article,
            'comments': comments,
            'form': form
        }
        return render(request, 'article_detail.html', context)


class CategoryIndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category_index.html', context)


class ArticleByCategoryIndexView(View):
    
    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs['category_pk'])
        articles = Article.objects.filter(category=category).order_by('-created_on')
        context = {
            'articles': articles,
            'category_name': category.name
        }
        return render(request, 'article_index.html', context)
        