from .zilean_mysql_access import zilean_sql, zilean_fetch_sql

_SHOW_DATA_BASES = "SHOW DATABASES;"
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


def _databases():
    pass

def _make_database():
    pass

def _remove_database():
    pass

def _tables():
    pass

def _tables_content():
    pass

def _make_table():
    pass

def _remove_table():
    pass

def _add_field():
    pass

def _remove_field():
    pass

def _change_field():
    pass

def _add_element():
    pass

def _remove_element():
    pass

def _get_element():
    pass
