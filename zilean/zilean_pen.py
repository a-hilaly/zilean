from .zilean_mysql_access import zilean_sql, zilean_fetch_sql
from .zilean_decorators import op_fails_repoter
from .zilean_jobs import _get_job as G

_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATA_BASE = "CREATE DATABASE {0};"
_DELETE_DATA_BASE = "DROP DATABASE {0};"
_USE_DATA_BASE = "USE {0};"
_SHOW_TABLE = "DESC {0};"
_SHOW_ALL_TABLES = "show tables;"
_CREATE_TABLE = "CREATE TABLE {0} ({1});"
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
_SHOW_TABLE_VALUES = "SELECT * FROM {0};"
_SELECT_GENERAL = """
    SELECT {0}
    FROM {1}
    WHERE {2};"""
_SELECT_VALUES_TABLE = "SELECT ({0}) FROM {1} WHERE {2};"

@op_fails_repoter(mode="zilean-op-type", job=G())
def _databases():
    return zilean_sql(_SHOW_DATABASES)

@op_fails_repoter(mode="zilean-op-type", job=G())
def _make_database(dbname):
    return zilean_sql(_CREATE_DATABASE.format(dbname))

@op_fails_repoter(mode="zilean-op-type", job=G())
def _remove_database(dbname):
    return zilean_sql(_DELETE_DATABASE.format(dbname))

@op_fails_reporter
def _tables(dbname):
    pass

@op_fails_reporter
def _tables_content(db, table):
    pass

@op_fails_reporter
def _make_table(db, table, **kwargs):
    pass

@op_fails_reporter
def _remove_table(db, table):
    pass

@op_fails_reporter
def _add_field(db, table, fieldname, fieldtype):
    pass

@op_fails_reporter
def _remove_field(db, table, fieldname):
    pass

@op_fails_reporter
def _change_field(db, table, fieldname, newfield, fieldtype):
    pass

@op_fails_reporter
def _add_element(db, table, **kwargs):
    pass

@op_fails_reporter
def _remove_element(db, table, **kwargs):
    pass

@op_fails_reporter
def _get_element(db, table, **kwargs):
    pass
