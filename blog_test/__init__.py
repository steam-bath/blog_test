from django.contrib import admin
from global_actions import *

admin.site.add_action(make_published, 'make_published')
admin.site.add_action(make_unpublished, 'make_unpublished')