from django.shortcuts import render
from .models import News

def news_page(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


def current_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news/current_news.html', {'news': news})