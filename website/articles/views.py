from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'articles/articles.html', {})