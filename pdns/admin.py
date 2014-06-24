from django.contrib import admin

from .models import (Cryptokeys, Domainmetadata, Domains, Record,
                     Supermasters, Tsigkeys)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'type', 'content', 'prio', 'ttl')
    list_filter = ('type',)


admin.site.register(Cryptokeys)
admin.site.register(Domainmetadata)
admin.site.register(Domains)
admin.site.register(Record, RecordAdmin)
admin.site.register(Supermasters)
admin.site.register(Tsigkeys)
