from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {
        'news': news,
        'title': 'Список новостей',
        'categories': categories})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    return render(request, 'news/category.html', {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
        'category': category
    })


def test(request):
    return HttpResponse('<h1>Tестовая страница</h1>')
