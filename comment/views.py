# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.urls	import reverse
from .models import Comment 
from .forms import CommentForm

# Create your views here.

# def update_comment(request):
# 	referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
	# if not request.user.is_authenticated:
	# 	return render(request, 'error.html', {'message': '用户未登录', 'redirect_to': referer})

	# text = request.POST.get('text', '').strip()
	# if text == '':
	# 	return render(request, 'error.html', {'message': '评论内容为空', 'redirect_to': referer})

	# try:
	# 	content_type  = request.POST.get('content_type', '')
	# 	object_id = int(request.POST.get('object_id', ''))
	# 	model_class = ContentType.objects.get(model=content_type).model_class()
	# 	model_obj = model_class.objects.get(pk = object_id)
	# except Exception as e:
	# 	return render(request, 'error.html', {'message': '评论对象不存在', 'redirect_to': referer})
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
    comment_form = CommentForm(request.POST, user=request.user)
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user 
        comment.save()

        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
        if not parent is None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if not comment.root is None else ' '
    else:
        #return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)