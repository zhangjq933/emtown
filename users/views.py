# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError

from .forms import LoginForm, RegForm, ContactForm

# Create your views here.
def login(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user = login_form.cleaned_data['user']
			auth.login(request, user)
			return redirect(request.GET.get('from', reverse('blog:index')))
	else:
		login_form = LoginForm()

	context = {}
	context['login_form'] = login_form
	return render(request, 'login.html', context)

def register(request):
	if request.method == 'POST':
		reg_form = RegForm(request.POST)
		if reg_form.is_valid():
			username = reg_form.cleaned_data['username']
			email = reg_form.cleaned_data['email']
			password = reg_form.cleaned_data['password']
			user = User.objects.create_user(username, email, password)
			user.save()
			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			return redirect(request.GET.get('from', reverse('blog:index')))
	else:
		reg_form = RegForm()

	context = {}
	context['reg_form'] = reg_form
	return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('blog:index')))

def contact(request):
	if request.method == 'POST':
		contactform = ContactForm(request.POST)
		if contactform.is_valid():
		    subject = request.POST.get('subject', '')
		    message = request.POST.get('message', '')
		    from_email = request.POST.get('from_email', '')
		    message = ("message:" + message +"\nEmail:" + from_email )
		    if subject and message and from_email:
		        try:
		            send_mail(subject, message,
		            				 'simulationfuture@sina.com', ['zhangjq0905@163.com'])
		        except BadHeaderError:
		            return HttpResponse('Invalid header found.')
		        return render(request, 'contact_done.html')
		    else:
		        # In reality we'd use a form class
		        # to get proper validation errors.
		        return HttpResponse('Make sure all fields are entered and valid.')
 	else:
 		contactform = ContactForm()		        

	context = {}	
	context['contactform'] = contactform
	return render(request, 'contact.html', context)


