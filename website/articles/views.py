from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from articles.models import Article


# Create your views here.
def blog_view(request):
    return render(request, 'articles/articles.html', {})


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'thumbnail', 'content']
    success_url = reverse_lazy('home')
