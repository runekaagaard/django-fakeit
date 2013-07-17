django-fakeit
=============

A management command that anonymizes the database. Fast. Only works for MySql.

Installation
============

Put the following in your requirements.txt file::

    git+git://github.com/runekaagaard/django-fakeit.git#egg=django-fakeit
    
And this in your ``settings.py`` file::

    FAKEIT_ALLOW = True

A good tip would be to use a ``settings_local.py`` file, to avoid nuking your
live database.

Usage
=====

A ``fakeit_settings.py`` must exist on the python path, and should contain::

    SETTINGS = {
        # These table will be emptied.
        'truncate': ['auth_message', 'django_admin_log', 'django_session', ],
        # These tables will be altered.
        'alter': [
            {
                # Tablename in the database of the table to alter.
                'table': 'persons_person',
                # These fields will be anonymized.
                'fields': {
                    # The callable CALLBACK1 should return a quoted name 
                    # surrounded with ``""``.
                    'name': CALLBACK1,
                    # The callable CALLBACK2 should return a number as a string.
                    'number': CALLBACK2,
                },
            },
            ... MORE TABLES GO HERE.
        # Which db engine to use.
        'db_engine': 'django.db.backends.mysql', 
    }
    
Callbacks
=========

The callbacks are responsible for creating the anonymized data. The return of
them are inserted directly into the SET command, so for string types should have
``""`` and be quoted.

A full example of fakeit_settings.py using the faker module could look like::

    from faker import Faker
    from random import randint
    FAKER = Faker()
    
    def name():
        return '"' + FAKER.name() + '"'
    
    def phone():
        return str(randint(10000000, 99999999))
        
    SETTINGS = {
        'truncate': ['auth_message', 'django_admin_log', 'django_session', ],
        'alter': [
            {
                'table': 'persons_person',
                'fields': {
                    'name': name,
                    'number': phone,
                },
            },
        'db_engine': 'django.db.backends.mysql', 
    }
    
