from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News

@login_required
def news_page(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


@login_required
def current_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news/current_news.html', {'news': news})