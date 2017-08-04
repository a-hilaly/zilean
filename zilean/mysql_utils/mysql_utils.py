from zilean.mysql_utils.mysql_access import (execute_only,
                                             execute_and_fetch)
from zilean.sys.models.zilean_rtype import _refetch_filter
from .mysql_query import (_SHOW_DATABASES,
                          _CREATE_DATABASE,
                          _DELETE_DATABASE,
                          _SHOW_TABLES,
                          _CREATE_TABLE,
                          _USE_DATABASE,
                          _DELETE_TABLE,
                          _IE_QUERY,
                          _SELECT_GENERAL,
                          _CT_QUERY)

# INSERT INTO `zilean_linked_databases` (`database`, `id_backups`) VALUES ( 'kikouuteeee', '["ddd"]' );

#@op_fails_reporter(mode="zilean-op-type", job=G())
@_refetch_filter([0])
def _databases():
    """
    return a list of strings containing msql databases
    =======================================================
    >>> from zilean.zilean_pen import _databases
    >>> _databases()
    ["sys", "mysql"]
    =======================================================
    """
    return execute_and_fetch(_SHOW_DATABASES)

#@op_fails_reporter(mode="zilean-op-type", job=G())
def _make_database(dbname):
    """
    make a mysql database
    =======================================================
    >>> _make_database('Table')
    =======================================================
    """
    return execute_only(_CREATE_DATABASE.format(dbname))

#@op_fails_reporter(mode="zilean-op-type", job=G())
def _remove_database(dbname):
    """
    Remove a mysql database
    =======================================================
    >>>
    """
    return execute_only(_DELETE_DATABASE.format(dbname))

#@op_fails_reporter
@_refetch_filter([0])
def _tables(dbname):
    """
    return a list of strings containing mysql tables at one
    given database
    =======================================================
    >>> _tables("sys")
    ["host_ip", "host_kappa" ... ""]
    =======================================================
    """
    return execute_and_fetch(_SHOW_TABLES.format(dbname))

#@op_fails_reporter
def _table_content(db, table):
    """
    return a 2 dimentioanl array containing all table values
    ========================================================
    >>> _table_content("sys", "host_ip")
    [[]]
    ========================================================
    """
    #XXX: uses : `select * from table`
    return execute_and_fetch(_SHOW_TABLE_VALUES.format(db, table))

#@op_fails_reporter
def _make_table(db, table, **kwargs):
    """
    Create a table at database with kwargs as fields
    =======================================================
    """
    return execute_only(_CT_QUERY(db, table, **kwargs))

#@op_fails_reporter
def _remove_table(db, table):
    """
    Drop table at db
    =======================================================
    """
    return execute_only(_DELETE_TABLE.format(db, table))

#@op_fails_reporter
def _add_field(db, table, field_name, field_type):
    """
    Add field to table at db
    =======================================================
    """
    return execute_only(_ADD_COLUMN.format(db, table, field_name, field_type))

#@op_fails_reporter
def _remove_field(db, table, field_name):
    """
    Remove field from table at db
    =======================================================
    """
    return execute_only(_DELETE_COLUMN.format(db, table, field_name))

#@op_fails_reporter
def _change_field(db, table, field_name, new_field, field_type):
    """
    Change field in table at db
    =======================================================
    """
    pass

#@op_fails_reporter
def _add_element(db, table, **kwargs):
    """
    add element to table at db
    =======================================================
    """
    return execute_only(_IE_QUERY(db, table, **kwargs), commit=True)

#@op_fails_reporter
def _remove_selection(db, table, with_limit=-1, **kwargs):
    """
    Remove Element from table at db
    =======================================================
    """
    return with_limit

#@op_fails_reporter
def _select_element(db, table, with_limit=-1, **kwargs):
    """
    Select elements that satisfy kwargs from table at db
    =======================================================
    """
    pass

def _select_element_opt(db, table, opt, **kwargs):
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
