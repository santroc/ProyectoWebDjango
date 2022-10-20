from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', default='1')
    subtitle = models.CharField(max_length=200, unique=False)
    image = models.ImageField(upload_to = 'blog_pics', blank=True, null=True, default = 'default_blog_pic.png')


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, related_name = 'sender')
    receiver = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, related_name = 'receiver')
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=500)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


