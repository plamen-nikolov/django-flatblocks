# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FlatBlock.header_en'
        db.add_column(u'flatblocks_flatblock', 'header_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatBlock.header_nl'
        db.add_column(u'flatblocks_flatblock', 'header_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatBlock.content_en'
        db.add_column(u'flatblocks_flatblock', 'content_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FlatBlock.content_nl'
        db.add_column(u'flatblocks_flatblock', 'content_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FlatBlock.header_en'
        db.delete_column(u'flatblocks_flatblock', 'header_en')

        # Deleting field 'FlatBlock.header_nl'
        db.delete_column(u'flatblocks_flatblock', 'header_nl')

        # Deleting field 'FlatBlock.content_en'
        db.delete_column(u'flatblocks_flatblock', 'content_en')

        # Deleting field 'FlatBlock.content_nl'
        db.delete_column(u'flatblocks_flatblock', 'content_nl')


    models = {
        u'flatblocks.flatblock': {
            'Meta': {'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'header_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'header_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['flatblocks']