from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Makes the entire database anonymous. DO NOT USE IN PRODUCTION."
    can_import_settings = True
    
    def handle(self, *app_labels, **options):
        from fakeit_settings import SETTINGS
        from django.conf import settings
        assert settings.FAKEIT_ALLOW == True, "FAKEIT_ALLOW needs to be True in your local_settings.py file."
        assert SETTINGS['db_engine'] == 'django.db.backends.mysql', "Not supported database engine."
        from django.db import connection, transaction
        cursor = connection.cursor()
        
        # Truncate tables.
        for table in SETTINGS['truncate']:
            cursor.execute("DELETE IGNORE FROM %s" % table)
            print "DELETED all rows in %s" % table
        del(table)
        
        # Alter tables.
        for cfg in SETTINGS['alter']:
            if not cfg['table']: continue
            cursor.execute("SELECT id from %s" % cfg['table'])
            i = 0
            print "Starting to alter %s" % cfg['table']
            for row in cursor.fetchall():
                i += 1
                sql = "UPDATE %s SET %s WHERE id=%d" % (
                    cfg['table'],
                    ",".join("%s=%s" % (k,v()) for k,v in cfg['fields'].items()),
                    row[0],
                )
                cursor.execute(sql)
            print "Altered %d rows in %s" % (i, cfg['table'])
        transaction.commit_unless_managed()
        