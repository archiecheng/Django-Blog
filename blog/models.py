from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class BlogComment(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)