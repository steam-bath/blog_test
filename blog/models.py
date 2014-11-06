# -*- coding: utf8 -*-
from django.db import models
from tinymce import models as tinymce_models
from ifcropper import ImageRatioField
from admin_fields import *
from django.core.validators import *

import datetime


class BlogTag(models.Model):
    """ Теги блога """

    # основные поля
    title = models.CharField(u'Заголовок', max_length=255, unique=True)

    # дополнительные поля
    is_active = models.BooleanField(u'Активность', default=True)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now(), editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'
        ordering = ['-id']


class BlogPost(models.Model):
    """ Статьи блога """

    # основные поля
    title = models.CharField(u'Заголовок', max_length=255)
    announce = tinymce_models.HTMLField(u'Анонс', max_length=255,
                                        help_text=u'Если оставить пустым - анонс будет загружен из текста статьи',
                                        blank=True)
    detail = tinymce_models.HTMLField(u'Текст')
    tags = models.ManyToManyField(BlogTag, verbose_name=u'Теги', related_name='posts')
    image = models.ImageField(verbose_name=u'Изображение', upload_to='blogpost/images', blank=True, null=True)
    preview_image = ImageRatioField('image', '150x150', verbose_name=u'Превью')

    # сео-поля
    seo_keywords = models.TextField('Keywords', max_length=255, blank=True)
    seo_description = models.TextField('Description', max_length=511, blank=True)

    # дополнительные поля
    is_active = models.BooleanField(u'Активность', default=True)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now(), editable=False)

    # укорачиваем анонс новости для списка
    def _short_announce(self):
        return short_announce(self.announce, 150)
    _short_announce.short_description = u'Анонс'
    _short_announce.allow_tags = True
    _short_announce.admin_order_field = '_short_announce'

    # кликабельное поле активности
    def _is_active(self):
        return ajax_isactive(self.is_active, self.pk)
    _is_active.short_description = u'Активность'
    _is_active.allow_tags = True
    _is_active.admin_order_field = 'is_active'

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        ordering = ['-id']


class BlogComment(models.Model):
    """ Комментарии к статье """

    # основные поля
    name = models.CharField(u'Имя', max_length=63, validators=[
        MinLengthValidator(2),   # минимальное кол-во символов
        MaxLengthValidator(50),  # максимальное кол-во символов
        RegexValidator('^\S+$'),  # всё, кроме пробелов
    ])
    text = models.TextField(u'Комментарий', max_length=255, validators=[
        MaxLengthValidator(256),  # максимальное кол-во символов
    ])
    post = models.ForeignKey(BlogPost, verbose_name=u'Статья')

    # дополнительные поля
    is_active = models.BooleanField(u'Активность', default=True)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now(), editable=False)

    def __unicode__(self):
        return '%s, %s...' % (self.name, self.text[:15])

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ['-id']