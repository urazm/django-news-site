from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')  # возможность поиска по заданным полям
    list_editable = ('is_published',)  # возможность редактирования прямо из списка
    list_filter = ('is_published', 'category')  # возможность фильтрации
    fields = ('title', 'content', 'is_published', 'category', 'get_photo', 'views', 'photo',
              'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'is_published', 'get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

