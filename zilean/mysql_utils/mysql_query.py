
# Databases querries
_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATABASE = "CREATE DATABASE {0};"
_DELETE_DATABASE = "DROP DATABASE {0};"
_USE_DATABASE = "USE {0};"

# Table querries
_SHOW_TABLE_FIELDS = "DESC {0}.{1};"
_SHOW_ALL_TABLES = "SHOW TABLES IN {0};"
_CREATE_TABLE = "CREATE TABLE {0} ({1}) ENGINE=InnoDB;"
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

_protocol_noprotocol = ' VARCHAR(10) NOT NULL,'
_protocol_taxon = {'s' : ' VARCHAR(10),',
                   'S' : ' VARCHAR(25),',
                   'j' : ' JSON',
                   'i' : ' INT(10),',
                   'I' : ' INT(25),',
                   'p' : ' PRIMARY KEY (`{0}`),',
                   'u' : ' UNIQUE KEY {0},',
                   't' : ' DEFAULT CURRENT_TIME_STAMP,',
                   'T' : ' DEFAULT CURRENT_TIME_STAMP ON UPDATE CURRENT_TIMESTAMP,',
                   'e' : ' ENUM({0}),'}

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

def _QIIT(table, fields=None, objects=None):
    pass
