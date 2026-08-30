from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    tag = models.ManyToManyField(Post)
    
