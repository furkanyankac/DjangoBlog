from django.shortcuts import redirect, render,HttpResponse,redirect,get_object_or_404, reverse
from sympy import re
from .forms import ArticleForm
from django.contrib import messages 
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_title = request.POST.get("comment_title")

        newComment = Comment(comment_author = comment_author , comment_title = comment_title)

        newComment.article = article
        newComment.save()
        
    return redirect(reverse("article:detail",kwargs={"id":id}))

@login_required(login_url="user:loginUser")
def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles": articles})
    else:
        articles = Article.objects.all()

    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

@login_required(login_url="user:loginUser")
def dashboard(request):

    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:loginUser")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makaleniz başarıyla eklendi.")
        return redirect("index")
    context = {
        "form":form
    }
    return render(request,"addarticle.html",context)

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()

    context = {
        "article": article,
        "comments": comments,
    }
    return render(request,"detail.html",context)

@login_required(login_url="user:loginUser")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance = article )    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makaleniz başarıyla güncellendi.")
        return redirect("index")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:loginUser")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()
    messages.success(request,"Makale başarıyla silinmiştir.")

    return redirect("article:dashboard")

