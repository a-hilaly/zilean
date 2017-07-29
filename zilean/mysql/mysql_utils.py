from zilean.mysql.mysql_access import (zilean_sql,
                                       zilean_fetch_sql)
from zilean.models.zilean_rtype import _refetch_filter
from .mysql_query import (_SHOW_DATABASES,
                          _CREATE_DATABASE,
                          _DELETE_DATABASE,
                          _CREATE_TABLE)


# INSERT INTO `zilean_linked_databases` (`database`, `id_backups`) VALUES ( 'kikouuteeee', '["ddd"]' );


#@op_fails_reporter(mode="zilean-op-type", job=G())
@_refetch_filter([1])
def _databases():
    """
    return a list of strings containing msql databases
    ================================================
    >>> from zilean.zilean_pen import _databases
    >>> _databases()
    ["sys", "mysql"]
    """
    return zilean_fetch_sql(_SHOW_DATABASES)

#@op_fails_reporter(mode="zilean-op-type", job=G())
def _make_database(dbname):
    """
    make a mysql database
    >>> _make_database('Table')
    ROW(0) AFFECTED !
    """
    return zilean_sql(_CREATE_DATABASE.format(dbname))

#@op_fails_reporter(mode="zilean-op-type", job=G())
def _remove_database(dbname):
    """
    Remove a mysql database
    """
    return zilean_sql(_DELETE_DATABASE.format(dbname))

#@op_fails_reporter
def _tables(dbname):
    """
    return a list of strings containing mysql tables at one given database
    >>> _tables("sys")
    ["host_ip", "host_kappa" ... ""]
    """
    return zilean_fetch_sql(_SHOW_ALL_TABLES.format(dbname))

#@op_fails_reporter
def _table_content(db, table):
    """
    return a 2 dimentioanl array containing all table values
    >>> _table_content("sys", "host_ip")
    [[]]
    """
    return zilean_fetch_sql(_SHOW_TABLE_VALUES.format(db, table))

#@op_fails_reporter
def _make_table(db, table, **kwargs):
    """
    Create a table at database with kwargs in format "field"="type,spe,len"
    """

#@op_fails_reporter
def _remove_table(db, table):
    """
    Drop table at database
    """
    pass

#@op_fails_reporter
def _add_field(db, table, fieldname, fieldtype):
    pass

#@op_fails_reporter
def _remove_field(db, table, fieldname):
    pass

#@op_fails_reporter
def _change_field(db, table, fieldname, newfield, fieldtype):
    pass

#@op_fails_reporter
def _add_element(db, table, **kwargs):
    pass

#@op_fails_reporter
def _remove_element(db, table, **kwargs):
    pass

#@op_fails_reporter
def _get_element(db, table, **kwargs):
    pass

#


def intern_fail_reporter():
    # Intern fail repoter
    pass


def zilean():
    pass

def unzilean():
    pass

def unzilean_ifempty():
    pass

def get_job():
    return 1

def incr_subjob():
    pass

def incr_job():
    pass

def set_job():
    pass
