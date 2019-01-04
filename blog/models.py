# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return (self.name)

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return (self.name)

class Article(models.Model):
	"""docstring for article"""
	title = models.CharField(max_length = 150)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	body = RichTextUploadingField(config_name='article_ckeditor')
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	tags = models.ManyToManyField(Tag, blank=True)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now_add=True	)
	views = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return (self.title)
	def increase_views(self	):
		self.views += 1
		self.save(update_fields=['views'])

	class Meta:
		ordering = ['-publish_time']
			