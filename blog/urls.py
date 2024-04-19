#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 11:51
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog/pub', views.pub_blog, name='pub_blog'),
]