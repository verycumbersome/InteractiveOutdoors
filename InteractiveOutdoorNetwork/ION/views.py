# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone

# from .forms import PostForm
from .models import Post, GearPost

class Main(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def timeline(request):
    return render(request, 'timeline.html', {})

def blog(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog.html', {
        'posts':posts
    })

def geartrade(request):
    gearposts = GearPost.objects.order_by('created_date')
    return render(request, 'geartrade.html', {
        'gearposts':gearposts
    })

def login(request):
    form = PostForm()
    return render(request, 'timeline.html', {'form': form})