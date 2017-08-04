import mysql.connector
from zilean.sys.models.zilean_rtype import ZileanOP
from zilean._logs import MYSQL_LOGS


#@op_fails_reporter(mode="normal", job="subjob")
def mysql_local_connection():
    """
    Return "LOCAL" MySQLConnection Cursor object
    ======================================================
    """
    try:
        return mysql.connector.connect(**MYSQL_LOGS,
                                       use_pure=True,
                                       raise_on_warnings=True).cursor()
    except:
        return -667

#@op_fails_reporter(mode="zilean-op-type", job="subjob")
def execute_only(*args, commit=False):
    """
    Execute a serie of queries to known cursor
    =====================================================
    >>> from zilean import execute_sql
    >>> from zilean import mysql_local_connection
    >>> crs = m()
    >>> execute_sql(query1, query2, cursor=crs).__call__()
    { "result" : '', "status" : -9999}
    =====================================================
    """
    try:
        cnx = mysql.connector.connect(**MYSQL_LOGS,
                                      use_pure=True,
                                      raise_on_warnings=True)
        cursor = cnx.cursor()
    except:
        return ZileanOP(None, -667)
    try:
        for query in list(args):
            cursor.execute(query)
        if commit:
            cnx.commit()
        return ZileanOP(None, -9999)
    except:
        return ZileanOP(None, -300)

def execute_and_fetch(*args, commit=False):
    """
    Execute a serie of queries to known cursor
    =====================================================
    >>> from zilean import execute_sql
    >>> from zilean import mysql_local_connection
    >>> crs = m()
    >>> execute_sql("SHOW DATABASE", cursor=crs).result
    [('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('zileansystem',)]
    =====================================================
    """
    result = []
    try:
        cnx = mysql.connector.connect(**MYSQL_LOGS,
                                      use_pure=True,
                                      raise_on_warnings=True)
        cursor = cnx.cursor()
    except:
        return ZileanOP(result, -667)
    try:
        for query in list(args):
            cursor.execute(query)
        for e in cursor:
            result.append(e)
        if commit:
            cnx.commit()
        return ZileanOP(result, -9999)
    except:
        return ZileanOP(result, -300)
