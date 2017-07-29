
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
