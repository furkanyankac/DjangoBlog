from tkinter import CASCADE
from tkinter.tix import Tree
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from sqlalchemy import null

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True, null = True, verbose_name = "Fotoğraf Ekle")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Makale", related_name = "comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_title = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_title
    class Meta:
        ordering = ['-comment_date']