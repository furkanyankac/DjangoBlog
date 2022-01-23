from csv import list_dialects
from pyexpat import model
from django.contrib import admin
from .models import Article, Comment

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","author"]

    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article

# Register your models here.
