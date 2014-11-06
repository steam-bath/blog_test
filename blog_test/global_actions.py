# -*- coding: utf8 -*-


# установить активность у объектов
def make_published(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_published.short_description = u"Активировать"


# снять активность у объектов
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_active=False)
make_unpublished.short_description = u"Убрать активность"
