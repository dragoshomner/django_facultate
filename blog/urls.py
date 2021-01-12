from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_index, name="article_index"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("categories/", views.category_index, name="category_index"),
    path("category/<int:category_pk>/", views.article_by_category_index, name="article_by_category_index"),
]