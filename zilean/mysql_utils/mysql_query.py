# Databases querries
_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATABASE = "CREATE DATABASE {0};"
_DELETE_DATABASE = "DROP DATABASE {0};"
_USE_DATABASE = "USE {0};"

# Table querries
_SHOW_TABLE_FIELDS = "DESC {0}.{1};"
_SHOW_TABLES = "SHOW TABLES IN {0};"

_CREATE_TABLE = """CREATE TABLE {0}.{1} (
{2}
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""

_DELETE_TABLE = "DROP TABLE {0}.{1};"

#COLUMN
_ADD_COLUMN = """ALTER TABLE {0}{1}
ADD {2} {3};"""
_DELETE_COLUMN = """ALTER TABLE {0}
DROP COLUMN {1};"""
_CHANGE_COLUMN = """
ALTER TABLE {0}
CHANGE {1} {2} {3};"""

_INSERT_VALUE_NO_MATCH = """INSERT INTO {0}.{1}
VALUES {2};"""

_INSERT_VALUE_WK = """INSERT INTO {0}.{1}
{2}
VALUES {3};"""

_SHOW_TABLE_VALUES = "SELECT * FROM {0}.{1};"
_SELECT_GENERAL = """
SELECT {0}
FROM {1}
WHERE {2};"""


# /!\ Warning in the next 2 functions :
# Using db or table as kwargs will
# cause some obvious conficlts

def _make_field_line2(a, b, comma=True, new_line=True):
    txt = None
    if "primary_key" in str(a):
        txt = "  PRIMARY KEY (`{0}`)".format(b) + "{0}"
    elif "unique_key" == a:
        txt = "  UNIQUE KEY (`{0}`)".format(b) + "{0}"
    else:
        txt = "  `{0}` {1}".format(a, b) + "{0}"

    if comma and new_line:
        return txt.format(",\n")
    elif comma and not new_line:
        return txt.format(",")
    elif (not comma) and new_line:
        return txt.format("\n")
    else:
        return txt.format("")

def _CT_QUERY(db=None, table=None, **kwargs):
    # Create Table Query
    n = len(kwargs)
    count = n
    comma = True
    new_line=True
    m = ""
    for field, _type in kwargs.items():
        if count < 2:
            comma = False
            new_line = False
        m += _make_field_line2(field, _type, comma=comma, new_line=new_line)
        count -= 1
    return _CREATE_TABLE.format(db, table, m)


def _tuplify_fields_sql(*t):
    targs = list(t)
    c = len(targs)
    r = "({0})"
    sample = "`{0}`"
    temp = ""
    for i in targs:
        temp += sample.format(i)
        if c > 1:
            temp += " ,"
        c -= 1
    return r.format(temp)

def _IE_QUERY(db, table, **kwargs):
    # Insert Element Query
    kwa = _tuplify_fields_sql(*kwargs.keys())
    rgs = str(tuple(kwargs.values()))
    return _INSERT_VALUE_WK.format(db, table, kwa, rgs)
