# coding: utf-8
from __future__ import absolute_import

from modeltranslation.translator import translator, TranslationOptions

from .models import FlatBlock

class FlatBlockTranslationOptions(TranslationOptions):
    fields = ('header', 'content',)

translator.register(FlatBlock, FlatBlockTranslationOptions)