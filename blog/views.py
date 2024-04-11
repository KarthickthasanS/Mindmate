from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from blog.models import Blog
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
import random
import re

def blog(request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs, 'current_page': 'blog'}
    return render(request, 'blog.html', context)



def blogpost (request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog, 'current_page': 'blogpost'}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)
    

    