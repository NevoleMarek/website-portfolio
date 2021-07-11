from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)
from django.urls import reverse_lazy

from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'thumbnail', 'content', 'description']
    success_url = reverse_lazy('blog')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'thumbnail', 'content', 'description']
    success_url = reverse_lazy('blog')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog')



class ArticleListView(ListView):
    model = Article
    paginate_by = 5



class ArticleDetailView(DetailView):
    model = Article
