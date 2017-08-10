from greww.shellenv import import_varenv
from greww.utils.pyshell import execute_shell_command as _esc

zileansqlpath = import_varenv("ZILEAN_SQL")
sql_api = "{0}/{1}".format(zileansqlpath, "_api.sh")
cmd = "bash {0}"

############################################@

def make_zilean_database():
    _esc(cmd.format("make_zilean_mysql"))

def clear_zilean_database():
    _esc(cmd.format("clear_zilean_mysql"))

def backup_database(**kwargs):
    for db, _file in kwargs.items():
        _esc(cmd.format("mysql_dump_database {0} {1}".format(db, _file)))

def backup_zilean_databases():
    _sql.backup_database(zileancache="usr/temp/b1")
    _sql.backup_database(zileansystem="usr/temp/b2")

def zilean_from_backup(bufilesys=None, bufilecache=None):
    _esc(cmd.format("{0} {1} {2}".format("zilean_mysql_frombackup",
                                         bufilesys,
                                         bufilecache)))

##############################################@

def zilean_mysql_maker(*args):
    g=""
    _esc(cmd.format("zilean_mysql_maker", gg))


def db_machines_maker(*args):
    g=""
    _esc(cmd.format("db_machines_maker"))
