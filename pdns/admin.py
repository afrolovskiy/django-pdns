from django.contrib import admin

from .models import (Cryptokey, Domainmetadata, Domain, Record,
                     Supermaster, Tsigkey)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'type', 'content', 'prio', 'ttl')
    list_filter = ('type',)


admin.site.register(Cryptokey)
admin.site.register(Domainmetadata)
admin.site.register(Domain)
admin.site.register(Record, RecordAdmin)
admin.site.register(Supermaster)
admin.site.register(Tsigkey)
