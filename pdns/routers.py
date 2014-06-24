class PowerDNSRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('django_pdns'):
            return 'powerdns'
        return 'default'

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)
