from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'thumbnail', 'content']
    success_url = reverse_lazy('blog')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'thumbnail', 'content']
    success_url = reverse_lazy('blog')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog')


class ArticleListView(ListView):
    model = Article
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
