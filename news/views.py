from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category
from .forms import NewsForm
from django.core.paginator import Paginator

# def test(request):
#     objects = ['john1', 'hello2', 'how are you3', 'can you read this bro?4', 'what5', 'hi6', 'john7']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)  # возвращает номер строки, при отсутствии присвается '1'
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'news/test.html', {
#         'page_obj': page_objects
#     })


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 3

    # extra_context = {
    #     'title': 'Главная'
    # }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # login_url = '/admin/' # Перейти на страницу авторизации, если не залогинен
    raise_exception = True  # Бросить 403(доступ запрещён) ошибку, если не залогинен










# def index(request):
#     news = News.objects.all()
#     return render(request, 'news/index.html', {
#         'news': news,
#         'title': 'Список новостей',
#         })


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {
#         'news': news,
#         'title': 'Список новостей',
#         'category': category,
#     })


# def view_news(request, news_id):
#     news_item = News.objects.get(pk=news_id)
#     return render(request, 'news/view_news.html', {
#         'news_item': news_item
#     })


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)  # Форма связанная с данными
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data) Когда используем несвяз.форму
#             news = form.save()  # Когда используем связанную форму
#             return redirect(news)
#     else:
#         form = NewsForm()              # Форма несвязанная с данными
#     return render(request, 'news/add_news.html', {
#         'form': form
#     })
