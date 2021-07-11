from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    thumbnail = models.ImageField(blank=True)
    description = models.TextField(max_length=500)
    content = models.TextField()
    
    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'pk':self.pk})