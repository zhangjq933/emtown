# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Comment(models.Model):
	"""docstring for Comment"""
	content_type = models.ForeignKey(ContentType, on_delete = models.DO_NOTHING)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	text = models.TextField()
	comment_time = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name='comments', on_delete = models.DO_NOTHING)

	root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.SET_NULL)
	parent = models.ForeignKey('self', related_name = 'parent_comment', null=True, on_delete=models.SET_NULL)
	reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['comment_time']
