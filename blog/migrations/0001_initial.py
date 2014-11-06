# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogTag'
        db.create_table(u'blog_blogtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 6, 0, 0))),
        ))
        db.send_create_signal(u'blog', ['BlogTag'])

        # Adding model 'BlogPost'
        db.create_table(u'blog_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('announce', self.gf('tinymce.models.HTMLField')(max_length=255, blank=True)),
            ('detail', self.gf('tinymce.models.HTMLField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('preview_image', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seo_keywords', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('seo_description', self.gf('django.db.models.fields.TextField')(max_length=511, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 6, 0, 0))),
        ))
        db.send_create_signal(u'blog', ['BlogPost'])

        # Adding M2M table for field tags on 'BlogPost'
        m2m_table_name = db.shorten_name(u'blog_blogpost_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False)),
            ('blogtag', models.ForeignKey(orm[u'blog.blogtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogpost_id', 'blogtag_id'])

        # Adding model 'BlogComment'
        db.create_table(u'blog_blogcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.BlogPost'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 6, 0, 0))),
        ))
        db.send_create_signal(u'blog', ['BlogComment'])


    def backwards(self, orm):
        # Deleting model 'BlogTag'
        db.delete_table(u'blog_blogtag')

        # Deleting model 'BlogPost'
        db.delete_table(u'blog_blogpost')

        # Removing M2M table for field tags on 'BlogPost'
        db.delete_table(db.shorten_name(u'blog_blogpost_tags'))

        # Deleting model 'BlogComment'
        db.delete_table(u'blog_blogcomment')


    models = {
        u'blog.blogcomment': {
            'Meta': {'ordering': "['-id']", 'object_name': 'BlogComment'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.BlogPost']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        u'blog.blogpost': {
            'Meta': {'ordering': "['-id']", 'object_name': 'BlogPost'},
            'announce': ('tinymce.models.HTMLField', [], {'max_length': '255', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 6, 0, 0)'}),
            'detail': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'preview_image': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seo_description': ('django.db.models.fields.TextField', [], {'max_length': '511', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts'", 'symmetrical': 'False', 'to': u"orm['blog.BlogTag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.blogtag': {
            'Meta': {'ordering': "['-id']", 'object_name': 'BlogTag'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['blog']