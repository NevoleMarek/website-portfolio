from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    template = 'pages/home.html'

    def get(self, request):
        return render(request, self.template, {})

class About(View):
    template = 'pages/about.html'

    def get(self, request):
        return render(request, self.template, {})

class Portfolio(View):
    template = 'pages/portfolio.html'

    def get(self, request):
        return render(request, self.template, {})