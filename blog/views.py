# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import	Article, Category
from blog.paginator import getPages 
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType 

from comment.models import Comment 
from comment.forms import CommentForm

# Create your views here.

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def index(request):
	articles = Article.objects.all()
	pages, articles = getPages(request, articles)
	context = {'articles': articles, 'pages': pages}
	return render(request, 'index.html', context)

def archive(request, year, month):
	articles = Article.objects.filter(publish_time__icontains=year+'-'+month).order_by('-publish_time')
	pages, articles = getPages(request, articles)
	context = {}
	context['articles'] = articles
	context['pages'] = pages 
	return render(request, 'index.html', context)

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	articles = Article.objects.filter(category=cate).order_by('-publish_time')
	pages, articles = getPages(request, articles)
	context = {}
	context['articles'] = articles
	context['pages'] = pages
	return render(request, 'index.html', context)

def detail(request, pk):
	context = {}
	article = get_object_or_404(Article, pk=pk)
	article.increase_views()
	blog_content_type = ContentType.objects.get_for_model(article)
	comments = Comment.objects.filter(content_type=blog_content_type, object_id=article.pk, parent=None)

	context['previous_blog'] = Article.objects.filter(publish_time__gt = article.publish_time).last()
	context['next_blog'] = Article.objects.filter(publish_time__lt = article.publish_time).first()
	context['article'] = article 
	context['comments'] = comments.order_by('-comment_time')
	context['comment_form'] = CommentForm(initial={'content_type': blog_content_type.model, 'object_id': pk, 'reply_comment_id': 0})
	return render(request, 'detail.html', context)

