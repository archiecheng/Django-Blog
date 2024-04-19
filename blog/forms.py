#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 12:24
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms

class PubBlogForm(forms.Form):
    title = forms.CharField(max_length=200, min_length=2)
    content = forms.CharField(min_length=2)
    category = forms.IntegerField()