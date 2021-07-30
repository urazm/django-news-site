from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {
        'news': news,
        'title': 'Список новостей',
        })


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {
        'news': news,
        'title': 'Список новостей',
        'category': category,
    })


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {
        'news_item': news_item
    })


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)  # Форма связанная с данными
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data) Когда используем несвяз.форму
            news = form.save()  # Когда используем связанную форму
            return redirect(news)
    else:
        form = NewsForm()              # Форма несвязанная с данными
    return render(request, 'news/add_news.html', {
        'form': form
    })
