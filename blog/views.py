# -*- coding: utf8 -*-
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from models import BlogPost, BlogTag, BlogComment
from forms import BlogCommentForm
from django.http import Http404
from django.contrib import messages

POSTS_PER_PAGE = 3
TAGS_PER_PAGE = 10


def post_list(request, page=1):
    """ Список статей блога """

    # загружаем статьи блога
    posts = BlogPost.objects.prefetch_related('tags').filter(is_active=True).order_by('-create_date')
    page_object = Paginator(posts, POSTS_PER_PAGE)
    try:
        curr_page_posts = page_object.page(page)
    except EmptyPage:
        raise Http404()

    # загружаем первые 10 тегов
    tags = BlogTag.objects.filter(is_active=True).order_by('title')[:10]

    return render(request, 'blogpost/list.html', {
        'posts': curr_page_posts,
        'pages': page_object.page_range,
        'active_page': int(page),
        'tags': tags,
    })


def post_detail(request, post_id):
    """ Статья детально """

    # добавление комментария
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            form.save(post_id)
            return redirect(request.path)
    else:
        form = BlogCommentForm()

    # загружаем статью
    try:
        # вместо get_object_or_404 применён метод get, чтобы можно было одним запросом загрузить все теги статьи
        post = BlogPost.objects.prefetch_related('tags').get(pk=post_id)
        comments = BlogComment.objects.filter(post=post, is_active=True).order_by('-create_date')
        # загружаем первые 10 тегов
        tags = BlogTag.objects.filter(is_active=True).order_by('title')[:10]
    except BlogPost.DoesNotExist:
        raise Http404()

    return render(request, 'blogpost/detail.html', {
        'post': post,
        'comments': comments,
        'tags': tags,
        'form': form,
    })


def tag_list(request, page=1):
    """ Список тегов блога """

    # загружаем теги блога
    tags = BlogTag.objects.prefetch_related('posts').filter(is_active=True).order_by('title')

    #from django.db import connection
    #print connection.queries

    page_object = Paginator(tags, TAGS_PER_PAGE)
    try:
        curr_page_tags = page_object.page(page)
    except EmptyPage:
        raise Http404()

    return render(request, 'blogtag/list.html', {
        'tags': curr_page_tags,
        'pages': page_object.page_range,
        'active_page': int(page),
    })


def tag_detail(request, tag_title, page=1):
    """ Тег детально """

    #загружаем тег
    try:
        # вместо get_object_or_404 применён метод get, чтобы можно было одним запросом загрузить все статьи тега
        tag = BlogTag.objects.prefetch_related('posts').get(title=tag_title)
        page_object = Paginator(tag.posts.all(), POSTS_PER_PAGE)
        try:
            curr_page_posts = page_object.page(page)
        except EmptyPage:
            raise Http404()
        # загружаем первые 10 тегов
        tags = BlogTag.objects.filter(is_active=True).order_by('title')[:10]
    except BlogTag.DoesNotExist:
        raise Http404()

    return render(request, 'blogtag/detail.html', {
        'tag': tag,
        'posts': curr_page_posts,
        'pages': page_object.page_range,
        'active_page': int(page),
        'tags': tags,
    })