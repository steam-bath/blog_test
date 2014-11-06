# -*- coding: utf8 -*-
from django.test import TestCase
from forms import BlogCommentForm
from models import BlogPost, BlogTag, BlogComment
from django.core.urlresolvers import reverse


def initialize_post_data():
    """ метод инициализирует временные тег и статью для выполнения тестов """

    # создаём тестовый тег
    tag = BlogTag.objects.create(
        title='test_tag'
    )
    # создаём тестовую статью
    post = BlogPost(
        title='test post',
        detail='lorem ipsum dolor sit amet'
    )
    post.save()
    post.tags.add(tag)
    return post


class BlogMethodTests(TestCase):

    def test_comment_post_blank_fields(self):
        """ Тестируем форму отправки комментария к статье с пустыми полями """

        # подготавливаем форму и убеждаемся в её невалидности
        form_data = {}
        form = BlogCommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comment_post_valid_form(self):
        """ Тестируем форму отправки комментария к статье с валидной формой """

        # подготавливаем валидную форму
        form_data = {
            'captcha_0': 'dummy-value',
            'captcha_1': 'PASSED',
            'name': u'Вася',
            'text': u'Тестовый комментарий',
        }
        form = BlogCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_post_invalid_field_values(self):
        """ Тестируем форму отправки комментария к статье с невалидным полем 'Имя' (менее двух символов) """

        # получаем тестовую статью
        post = initialize_post_data()

        # пытаемся отправить форму с невалидными данными
        form_data = {'name': 'A'}
        response = self.client.post(reverse('blog:post_detail', kwargs={'post_id': post.pk}), form_data)
        self.assertFormError(response, 'form', 'name', u'Имя не может быть меньше 2 символов!')

    def test_comment_add_to_database(self):
        """ Тестируем сохранение комментария в базу данных через форму """

        # получаем тестовую статью
        post = initialize_post_data()

        # подготавливаем валидную форму
        form_data = {
            'captcha_0': 'dummy-value',
            'captcha_1': 'PASSED',
            'name': u'Петя',
            'text': u'Тестовый комментарий',
        }
        form = BlogCommentForm(form_data)
        comment = form.save(post.pk)
        self.assertEquals(comment, BlogComment.objects.get(name=u'Петя', text=u'Тестовый комментарий'))