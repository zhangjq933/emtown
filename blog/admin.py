# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Article, Category, Tag

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'author', 'publish_time']

admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Author)