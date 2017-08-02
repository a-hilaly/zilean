import mysql.connector
from zilean.sys.models.zilean_rtype import ZileanOP
from zilean._logs import MYSQL_LOGS

# Take tuple or list or 5 elements
#@op_fails_reporter(mode="normal", job="subjob")
def mlogs_mysql_connection(*mlogs):
    """
    Return MySQLConnection Cursor object that can directly
    execute MySQL querries
    ======================================================
    >>> from zilean import mlogs_mysql_connection
    >>> logs = ('localhost', 22, 'root', 'uehMLMRw', True, True)
    >>> cursor = mlogs_mysql_connection(*logs)
    >>> cursor.execute("SHOW DATABASES")
    ======================================================
    """
    try:
        host, port, user, password, use_pure, row = mlogs
        return mysql.connector.connect(host=host,
                                       user=user,
                                       password=password,
                                       use_pure=use_pure,
                                       raise_on_warnings=row)
    except:
        return -666

#@op_fails_reporter(mode="normal", job="subjob")
def kwargs_mysql_connection(host=None,
                            port=None,
                            user=None,
                            password=None,
                            use_pure=True,
                            raise_on_warnings=True):
    """
    Works like mlogs_mysql_connection but with different
    arguments.
    ======================================================
    """
    try:
        return mysql.connector.connect(host=host,
                                       port=port,
                                       user=user,
                                       password=password,
                                       use_pure=use_pure,
                                       raise_on_warnings=raise_on_warnings)
    except:
        return -666

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
def execute_only_sql(*args):
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
        return ZileanOP(None, -9999)
    except:
        return ZileanOP(None, -300)

def execute_and_fetch_sql(*args):
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
        return ZileanOP(result, -9999)
    except:
        return ZileanOP(result, -300)
