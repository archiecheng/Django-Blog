from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='CategoryName')

    def __str__(self):
        return self.name

    class Meta:
        # apple, apples
        verbose_name = 'BlogCategories'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(verbose_name='content')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='pub_date')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')

    def __str__(self):
        return self.title

    class Meta:
        # apple, apples
        verbose_name = 'blog'
        verbose_name_plural = verbose_name
        ordering = ['-pub_time']


class BlogComment(models.Model):
    content = models.TextField(verbose_name='content')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='pub_date')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')

    def __str__(self):
        return self.content

    class Meta:
        # apple, apples
        verbose_name = 'comment'
        verbose_name_plural = verbose_name
        ordering = ['-pub_time']
