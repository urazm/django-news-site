from django.contrib import admin
from .models import News,Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')  # возможность поиска по заданным полям
    list_editable = ('is_published',)  # возможность редактирования прямо из списка
    list_filter = ('is_published', 'category')  # возможность фильтрации


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

