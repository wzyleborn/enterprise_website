from django.http import HttpResponse
from django.shortcuts import render

from news.models import News


def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request,'list.html',{'news_list':news_list})

def news_detail(request,id):
    try:
        news = News.objects.get(id=id)
        return render(request,'detail.html',{'news':news})
    except News.DoesNotExist:
        return render(request,'404.html')