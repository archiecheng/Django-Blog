#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 13:30
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'zlauth'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email_captcha')
]
