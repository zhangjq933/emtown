# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models	import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'content_object', 'text', 'comment_time', 'root', 'parent', 'reply_to','user')