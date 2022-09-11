from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'details.html', {'post': post})


def about(request):
    aboutus = ""
    return render(request, 'about.html', {'aboutus': aboutus})


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form': form})


def editpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'editpost.html', {'form': form})


def addcomment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.published_date = timezone.now()
            form.save()
            return redirect('details', pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'addcomment.html', {'form': form})

