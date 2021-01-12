from django.urls import path
from . import views
from blog.views import (
    ArticleIndexView,
    CommentCreateView,
    ArticleDetailsView,
    CategoryIndexView,
    ArticleByCategoryIndexView
)

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="article_index"),
    path("articles/<int:pk>/", ArticleDetailsView.as_view(), name="article_detail"),
    path("articles/categories/", CategoryIndexView.as_view(), name="category_index"),
    path("articles/category/<int:category_pk>/", ArticleByCategoryIndexView.as_view(), name="article_by_category_index"),
    path('articles/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
]