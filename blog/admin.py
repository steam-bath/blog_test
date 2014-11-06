# -*- coding: utf8 -*-
from models import BlogPost, BlogTag, BlogComment
from django.contrib import admin
from admin_classes import BlogTestAdmin
from ifcropper import ImageCroppingMixin


class CommentsInline(admin.StackedInline):
    model = BlogComment
    extra = 0


class BlogPostAdmin(ImageCroppingMixin, BlogTestAdmin):
    """ Статьи блога """

    inlines = [CommentsInline]

    # список
    list_display = ('title', '_short_announce', 'create_date', '_is_active')

    # карточка
    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {'fields': ['title', 'announce', 'detail', 'tags']}),
            (None, {'fields': [('is_active', 'create_date')], 'classes': []}),
            (u'Графическая информация', {'fields': ['image', 'preview_image']}),
        ]
        if obj and (obj.seo_keywords or obj.seo_description):
            fieldsets.append((u'Сео-теги', {'fields': ['seo_keywords', 'seo_description']}))
        else:
            fieldsets.append((u'Сео-теги', {'fields': ['seo_keywords', 'seo_description'], 'classes': ('collapse',)}))

        return fieldsets

    date_hierarchy = 'create_date'

    search_fields = ['title', 'announce', 'detail']

    list_filter = ['is_active']

    filter_horizontal = ('tags',)

    readonly_fields = ('create_date',)


class BlogTagAdmin(admin.ModelAdmin):
    """ Теги блога """

    # не показывать модель в административном интерфейсе
    def get_model_perms(self, request):
        return {}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogTag, BlogTagAdmin)