from __future__ import unicode_literals

from django.db import models

DOMAIN_TYPE_CHOICES = (
    ('NATIVE', 'native'),
    ('MASTER', 'master'),
)

RECORD_TYPE_CHOICES = (
    ('A', 'A'),
    ('AAAA', 'AAAA'),
    ('AFSDB', 'AFSDB'),
    ('CERT', 'CERT'),
    ('CNAME', 'CNAME'),
    ('DNSKEY', 'DNSKEY'),
    ('DS', 'DS'),
    ('HINFO', 'HINFO'),
    ('KEY', 'KEY'),
    ('LOC', 'LOC'),
    ('MX', 'MX'),
    ('NAPTR', 'NAPTR'),
    ('NS', 'NS'),
    ('NSEC', 'NSEC'),
    ('PTR', 'PTR'),
    ('RP', 'RP'),
    ('RRSIG', 'RRSIG'),
    ('SOA', 'SOA'),
    ('SPF', 'SPF'),
    ('SSHFP', 'SSHFP'),
    ('SRV', 'SRV'),
    ('TXT', 'TXT'),
)


class Cryptokey(models.Model):
    domain = models.ForeignKey('Domain', blank=True, null=True)
    flags = models.IntegerField()
    active = models.NullBooleanField()
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'cryptokeys'
        verbose_name = 'crypto key'


class Domainmetadata(models.Model):
    domain = models.ForeignKey('Domain', blank=True, null=True)
    kind = models.CharField(max_length=16, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'domainmetadata'
        verbose_name = 'domain metadata'
        verbose_name_plural = 'domain metadata'


class Domain(models.Model):
    name = models.CharField(unique=True, max_length=255)
    master = models.CharField(max_length=20, blank=True)
    last_check = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=6, choices=DOMAIN_TYPE_CHOICES)
    notified_serial = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'domains'

    def __unicode__(self):
        return self.name


class Record(models.Model):
    domain = models.ForeignKey(Domain, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=10, blank=True,
                            choices=RECORD_TYPE_CHOICES)
    content = models.CharField(max_length=255, blank=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    change_date = models.IntegerField(blank=True, null=True)
    ordername = models.CharField(max_length=255, blank=True)
    auth = models.NullBooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'records'

    def __unicode__(self):
        return "%s %s %s" % (self.type, self.name, self.content)


class Supermaster(models.Model):
    ip = models.CharField(max_length=25)
    nameserver = models.CharField(primary_key=True, max_length=255)
    account = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'supermasters'
        unique_together = (
            ('ip', 'nameserver'),
        )

    def __unicode__(self):
        return self.nameserver


class Tsigkey(models.Model):
    name = models.CharField(max_length=255, blank=True)
    algorithm = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tsigkeys'
        verbose_name = 'TSIG key'
