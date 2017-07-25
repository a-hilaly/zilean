from .zilean_mysql_access import (zilean_sql,
                                  zilean_fetch_sql)

from .zilean_rtype import _refetch_filter

_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATA_BASE = "CREATE DATABASE {0};"
_DELETE_DATA_BASE = "DROP DATABASE {0};"
_USE_DATA_BASE = "USE {0};"
_SHOW_TABLE_FIELDS = "DESC {0}.{1};"
_SHOW_ALL_TABLES = "show tables;"
_SHOW_ALL_TABLES = "SHOW TABLES IN {0};"
_CREATE_TABLE = "CREATE TABLE {0} ({1}) ENGINE=InnoDB;"

def _QCT(name, fields):
    _funquery = ''
    for field in fields:
        if ':' in field:
            code, field1 = field.split(':')
            _funquery += ' ' + field1
            for c in code:
                _funquery += _protocol_taxon[c].format(field1)
        else:
            _funquery += ' ' + field + _protocol_noprotocol
    _query = _CREATE_TABLE.format(name, _funquery)
    return _query[s0:-3] + _query[-2:]

_DELETE_TABLE = "DROP TABLE {0};"
_ADD_COLUMN = """
    ALTER TABLE {0}
    ADD {1} {2};"""
_DELETE_COLUMN = """
    ALTER TABLE {0}
    DROP COLUMN {1};"""
_CHANGE_COLUMN = """
    ALTER TABLE {0}
    CHANGE {1} {2} {3};"""

_ADD_VALUE = "INSERT INTO {0} VALUES ({1});"
_ADD_VALUE_WK = "INSERT INTO {0} ({1}) VALUES ({2});"

_SHOW_TABLE_VALUES = "SELECT * FROM {0}.{1};"

_SELECT_VALUES_TABLE = "SELECT ({0}) FROM {1} WHERE {2};"

#@op_fails_reporter(mode="zilean-op-type", job=G())
@_refetch_filter([1])
def _databases():
    """
    return a list of strings containing mysql databases names"
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

def op_fails_reporter(mode="", job=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            if job == "subjob":
                incr_subjob()
            else:
                incr_job()
            job = get_job()
            res = func(*args, **kwargs)
            t = time.ctime()
            if isinstance(res, ZileanOP):
                if res.status != -9999:
                    report_fail(func, job, t, res.status, res.out_put, args=args, kwargs=kwargs)
            return res
        return wrap_args
    return wrap_func


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
