from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/static/articles/img/", blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default=None)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, default=None)

class Author(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=250)