# -*- coding: utf8 -*-
from django import forms
from captcha.fields import CaptchaField
from models import BlogComment


class BlogCommentForm(forms.ModelForm):
    """ Форма добавления комментария """

    # дополнительные поля формы
    captcha = CaptchaField(required=True, error_messages={
        'required': u"Это обязательно поле!",
        'invalid': u"Введите код ещё раз",
    })

    class Meta:
        model = BlogComment
        exclude = ['post', 'is_active']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 6, 'maxlength': 256}),
        }
        error_messages = {
            'name': {
                'max_length': u"Имя не может быть больше 50 символов!",
                'min_length': u"Имя не может быть меньше 2 символов!",
                'invalid': u"Имя не должно содержать пробелы",
                'required': u"Это обязательно поле!",
            },
            'text': {
                'max_length': u"Комментарий не может быть больше 255 символов!",
                'required': u"Это обязательно поле!",
            },
        }

    def save(self, post_id=None, commit=True):
        """ Добавление нового комментария """

        comment = super(BlogCommentForm, self).save(commit=False)
        comment.post_id = post_id
        if commit:
            comment.save()
        return comment