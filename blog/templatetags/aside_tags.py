from django import template
from ..models import Article, Category

register = template.Library()

@register.simple_tag
def get_recent_articles(num=5):
	return Article.objects.all().order_by('-publish_time')[:num]

@register.simple_tag
def archives():
	return Article.objects.dates('publish_time', 'month', order='DESC')

@register.simple_tag
def categorys():
	return Category.objects.all()