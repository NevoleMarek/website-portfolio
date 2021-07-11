from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleListView,
    ArticleDetailView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article-edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail')
]
