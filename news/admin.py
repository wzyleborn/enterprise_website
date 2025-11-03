from django.contrib import admin

from news.models import Category, News


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_at','updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)