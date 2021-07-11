from django.urls import path

from .views import (
    blog_view,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
    path('', blog_view, name='blog'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article-edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete')
]
