"""emtown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^archive/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.archive, name = 'archive'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name = 'category'),
    url(r'^about/$', views.about, name = 'about'),
]
