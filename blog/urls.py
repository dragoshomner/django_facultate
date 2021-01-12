from django.urls import path
from . import views
from blog.views import (
    ArticleIndexView,
    CommentCreateView,
    ArticleDetailsView,
    CategoryIndexView,
    ArticleByCategoryIndexView,
    RegisterView,
    LoginView,
    LogoutView, 
    CommentEditView,
    MyCommentsIndexView,
    CommentDeleteView
)

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="article_index"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("articles/<int:pk>/", ArticleDetailsView.as_view(), name="article_detail"),
    path("articles/categories/", CategoryIndexView.as_view(), name="category_index"),
    path("articles/category/<int:category_pk>/", ArticleByCategoryIndexView.as_view(), name="article_by_category_index"),
    path('articles/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk_comment>/edit', CommentEditView.as_view(), name='comment_edit'),
    path('my-comments', MyCommentsIndexView.as_view(), name='my_comments'),
    path('comment/<int:pk_comment>/delete', CommentDeleteView.as_view(), name='comment_delete'),
]