from django.urls import path

from .views import (
    blog_view,
    ArticleCreateView
)

urlpatterns = [
    path('', blog_view, name='blog'),
    path('create/', ArticleCreateView.as_view(), name='article-create')
]
