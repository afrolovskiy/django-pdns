django-pdns
===========

Basic Django app that connects to the database used by the MySQL and PostgreSQL backends for PowerDNS.


Usage
-----

Add 'pdns' to your INSTALLED_APPS and add a key 'powerdns' to the DATABASES dict in your projects' settings, e.g.:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'powerdns': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdns',
        'USER': 'pdns',
        'PASSWORD': 'supercomplicatedpassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Finally, add pdns.routers.PowerDNSRouter to your DATABASE_ROUTERS list.
