# -*- coding: utf8 -*-

"""
Класс-рендер административного интерфейса для моделей
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns
from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json


class BlogTestAdmin(admin.ModelAdmin):
    """
    Административный класс BlogTestAdmin
    Применение:
        a) позволяет переключать активность записей в форме списка записей
    """

    class Media:
        js = (
            'admin/js/jquery.js',
            'admin/js/form_list_actions.js'
        )

    def get_urls(self):
        """ подключаем url для обработки метода change_activity """
        model_urls = super(BlogTestAdmin, self).get_urls()
        extra_urls = patterns('',
            url(r'^change_activity/$', self.change_activity),
        )
        return extra_urls + model_urls

    @csrf_exempt
    def change_activity(modelAdmin_class, request):
        """ Ajax: изменить активность элемента """

        try:
            element = modelAdmin_class.get_object(request, request.POST.get('element_id', 0))
            if element:
                if not element.is_active:
                    icon = '%sadmin/img/icons/icon-yes.gif' % (settings.STATIC_URL)
                    alt = 'Активно'
                    element.is_active = True
                else:
                    element.is_active = False
                    icon = '%sadmin/img/icons/icon-no.gif' % (settings.STATIC_URL)
                    alt = 'Выключено'

                element.save()
                result = 1
        except Exception:
            result = 0
            icon = '%sadmin/img/icons/icon_alert.gif' % (settings.STATIC_URL)
            alt = 'Ошибка'

        return HttpResponse(json.dumps({'result': result, 'icon': icon, 'alt': alt}), content_type="application/json")