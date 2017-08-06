from __future__ import print_function
import sys
import mysql.connector
from zilean.sys.models.zilean_rtype import ZileanOP
from zilean._logs import MYSQL_LOGS


class ConnectorsRegister():

    __slots__ = ["connectors"]

    def __init__(self):
        self.connectors = set()

    @property
    def gen(self):
        return self.connectors.copy().pop()

    @property
    def is_empty(self):
        return len(self.connectors) == 0

    def _register(self, cntr):
        self.connectors.add(cntr)

    def _new(self):
        self.connectors.add(mysql_local_connector())

    def _reset(self):
        self.connectors.clear()
        self._new()

_connectors = ConnectorsRegister()

def connector_register(func):
    global _connectors
    c = func()
    _connectors._register(c)
    return c


def with_connectors_register(func):
    def wrap_args(*args,**kwargs):
        global _connectors
        if _connectors.is_empty:
            _connectors._new()
        kwargs["connector"] = _connectors.gen
        res = func(*args, **kwargs)
        return res
    return wrap_args

def pure_connector_underfails(*errors):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            for error in errors:
                if res.status == error:
                    kwargs["connector"] = mysql_local_connector()
                    return func(*args, **kwargs)
            return res
        return wrap_args
    return wrap_func


@connector_register
def mysql_local_connector():
    """
    Return "LOCAL" MySQLConnection Cursor object
    ======================================================
    """
    try:
        return mysql.connector.connect(**MYSQL_LOGS,
                                       use_pure=True,
                                       raise_on_warnings=True)
    except:
        return -667

@pure_connector_underfails(-669, -668)
@with_connectors_register
def execute_only(*args, commit=False, connector=None):
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
        cursor = connector.cursor()
    except:
        return ZileanOP(None, -668)
    try:
        for query in list(args):
            cursor.execute(query)
        if commit:
            connector.commit()
        return ZileanOP(None, -9999)
    except ReferenceError:
        return ZileanOP(None, -669)
    except:
        return ZileanOP(None, -300)


@pure_connector_underfails(-667, -669)
@with_connectors_register
def execute_and_fetch(*args, commit=False, connector=None):
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
        cursor = connector.cursor()
    except:
        return ZileanOP(result, -667)
    try:
        for query in list(args):
            cursor.execute(query)
        for e in cursor:
            result.append(e)
        if commit:
            connector.commit()
        return ZileanOP(result, -9999)
    except ReferenceError:
        return ZileanOP(None, -669)
    except:
        return ZileanOP(result, -300)
