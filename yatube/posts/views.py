from django.shortcuts import render, get_object_or_404
from .models import Post, Group

posts_count = 10  # Кол-во выводимых постов


def index(request):
    posts = Post.objects.select_related('group').all()[:posts_count]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.posts.all()[:posts_count]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
