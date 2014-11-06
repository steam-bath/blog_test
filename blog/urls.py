# -*- coding: utf8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    # список статей блогов
    url(r'^$', 'post_list', name='post_list'),
    url(r'^page/(?P<page>[1-9]\d*)/$', 'post_list', name='post_pagination'),

    # карточка статьи блога
    url(r'^(?P<post_id>[1-9]\d*)/$', 'post_detail', name='post_detail'),

    # список тегов блога
    url(r'^tag/$', 'tag_list', name='tag_list'),
    url(r'^tag/page/(?P<page>[1-9]\d*)/$', 'tag_list', name='tag_pagination'),

    # карточка тега блога
    url(r'^tag/(?P<tag_title>[\w\s-]+)/$', 'tag_detail', name='tag_detail'),
    url(r'^tag/(?P<tag_title>[\w\s-]+)/page/(?P<page>[1-9]\d*)/$', 'tag_detail', name='tag_detail_pagination'),
)
