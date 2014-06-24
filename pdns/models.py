# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

DOMAIN_TYPE_CHOICES = (
    ('NATIVE', 'native'),
    ('MASTER', 'master'),
)


class Cryptokeys(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey('Domains', blank=True, null=True)
    flags = models.IntegerField()
    active = models.NullBooleanField()
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'cryptokeys'
        verbose_name = 'crypto key'


class Domainmetadata(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey('Domains', blank=True, null=True)
    kind = models.CharField(max_length=16, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'domainmetadata'
        verbose_name = 'domain metadata'
        verbose_name_plural = 'domain metadata'


class Domains(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    master = models.CharField(max_length=20, blank=True)
    last_check = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=6, choices=DOMAIN_TYPE_CHOICES)
    notified_serial = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'domains'
        verbose_name = 'domain'

    def __unicode__(self):
        return self.name


class Record(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey(Domains, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=10, blank=True)
    content = models.CharField(max_length=255, blank=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    change_date = models.IntegerField(blank=True, null=True)
    ordername = models.CharField(max_length=255, blank=True)
    auth = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'records'

    def __unicode__(self):
        return "%s %s %s" % (self.type, self.name, self.content)


class Supermasters(models.Model):
    ip = models.CharField(max_length=25)
    nameserver = models.CharField(primary_key=True, max_length=255)
    account = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'supermasters'
        verbose_name = 'supermaster'
        unique_together = (
            ('ip', 'nameserver'),
        )

    def __unicode__(self):
        return self.nameserver


class Tsigkeys(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    algorithm = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tsigkeys'
        verbose_name = 'TSIG key'
