# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Address.mobile'
        db.alter_column('addressbook_address', 'mobile', self.gf('django.db.models.fields.BigIntegerField')())
    def backwards(self, orm):

        # Changing field 'Address.mobile'
        db.alter_column('addressbook_address', 'mobile', self.gf('django.db.models.fields.IntegerField')())
    models = {
        'addressbook.address': {
            'Meta': {'object_name': 'Address'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.BigIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['addressbook']