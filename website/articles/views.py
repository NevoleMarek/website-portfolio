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

    TRUNC_LEN = 500

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        for i in ctx['object_list']:
            i.content_short = i.content[:self.TRUNC_LEN]
            if len(i.content) > self.TRUNC_LEN:
                i.content_short += '...'
        return ctx


class ArticleDetailView(DetailView):
    model = Article
