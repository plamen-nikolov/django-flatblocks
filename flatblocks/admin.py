from django.contrib import admin
from flatblocks.models import FlatBlock

from modeltranslation.admin import TranslationAdmin

class FlatBlockAdmin(TranslationAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')

admin.site.register(FlatBlock, FlatBlockAdmin)
