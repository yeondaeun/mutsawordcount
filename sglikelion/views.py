from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sglikelion/post_list.html', {'posts': posts})

def post_detail(request, index):
    post = get_object_or_404(Post, pk=index)
    return render(request, 'sglikelion/post_detail.html', {'post': post})

def post_new(request):      #request에는 우리가 입력했던 데이터들을 가지고 있다
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', index=post.pk)
    else:
        form = PostForm()
    return render(request, 'sglikelion/post_edit.html', {'form': form})


def post_edit(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', index=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sglikelion/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'sglikelion/post_draft_list.html', {'posts': posts})

def post_publish(request, index):
    post = get_object_or_404(Post, pk=index)
    post.publish()
    return redirect('post_detail', index=index)