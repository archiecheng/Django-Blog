#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 20:33
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from django.contrib.auth import get_user_model
from .models import  CaptchaModel
User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': 'Please enter username',
        'max_length': 'Username length is between 2 and 20',
        'min_length': 'Username length is between 2 and 20'
    })
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email',
        'invalid': 'Please enter a correct email address'
    })
    captcha = forms.CharField(max_length=4, min_length=4)
    password = forms.CharField(max_length=20, min_length=4)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('The email address has been registered!')
        return email


    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')
        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError('Verification code and email address do not match')
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email',
        'invalid': 'Please enter a correct email address'
    })
    password = forms.CharField(max_length=20, min_length=4)
    remember = forms.IntegerField(required=False)
