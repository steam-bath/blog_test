# -*- coding: utf8 -*-

"""
Сборник административных полей для моделей
"""

from django.conf import settings
import datetime


def short_announce(announce, length):
    """ Показывает укороченный анонс для страницы списка """

    if len(announce) > length:
        return '<div title="'+announce+'">'+announce[:length-3]+'...'+'</div>'
    else:
        return '<div title="'+announce+'">'+announce+'</div>'


def ajax_isactive(is_active, id):
    """ Кликабельная иконка активности элемента для страницы списка """

    if not is_active:
        icon = 'icon-no.gif'
        alt = 'Выключено'
    else:
        icon = 'icon-yes.gif'
        alt = 'Активно'

    return '<a class="_is_active" href="javascript:void(0);">' \
           '<img height="10px" width="10px" src="%sadmin/img/icons/%s" alt="%s">' \
           '<input type="hidden" name="element_id" value="%d" />' \
           '</a>' % (settings.STATIC_URL, icon, alt, id)