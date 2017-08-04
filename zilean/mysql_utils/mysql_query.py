
def _get_protocols():
    pass

# Databases querries
_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATABASE = "CREATE DATABASE {0};"
_DELETE_DATABASE = "DROP DATABASE {0};"
_USE_DATABASE = "USE {0};"

# Table querries
_SHOW_TABLE_FIELDS = "DESC {0}.{1};"
_SHOW_ALL_TABLES = "SHOW TABLES IN {0};"

_CREATE_TABLE = """
CREATE TABLE {0}.{1} (
{2}
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""

# /!\ Warning in the next 2 functions :
# Using db or table as kwargs will
# cause some obvious conficlts
def _dp(s, mode=None):
    # decode dict protocol
    s1 = s
    s2 = s
    return s1, s2

def _make_field_line2(a, b, comma=True, new_line=True):
    if comma and new_line:
        return "  `{0}` {1},\n".format(a, b)
    elif comma and not new_line:
        return "  `{0}` {1},".format(a, b)
    elif (not comma) and new_line:
        return "  `{0}` {1}\n".format(a, b)
    else:
        return "  `{0}` {1}".format(a, b)

def _make_extra_line2(protocol, target=None, ):
    pass

def _p_cqt(db=None, table=None, **kwargs):
    # protocol call
    nkwargs, properties = _dp(kwargs, mode="safe")
    n = len(nkwargs)
    count = n
    comma = True
    new_line=True
    m = ""
    for field, _type in nkwargs.items():
        if count < 2:
            comma = False
            new_line = False
        m += _make_field_line2(field, _type, comma=comma, new_line=new_line)
        count -= 1
    return _CREATE_TABLE.format(db, table, m)


def _ha_cqt(db=None, table=None, **kwargs):
    # half assisted
    pass

_DELETE_TABLE = "DROP TABLE {0};"

#COLUMN
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

def _QCT(db, name, fields):
    _funquery = ''
    for field in fields:
        if ':' in field:
            code, field1 = field.split(':')
            _funquery += ' ' + field1
            for c in code:
                _funquery += _protocol_taxon[c].format(field1)
        else:
            _funquery += ' ' + field + _protocol_noprotocol
    _query = _CREATE_TABLE.format(db, name, _funquery)
    return _query[0:-3] + _query[-2:]

def _QCT_KW(db, name, **kwargs):
    return _QCT(db,
                name,
                ["{0}:{1}".format(j, i) for i, j in kwargs.items()])


def _QIIT(table, fields=None, objects=None):
    pass
