from django.urls import  path

from articles.views import blog_view

urlpatterns = [
    path('', blog_view, name='blog')
]