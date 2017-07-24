import pymysql.cursors
from .zilean_rtype import ZileanOP
from .zilean_decorators import op_fails_repoter
from .zilean_jobs import _get_job as G

# -666 Mysql connection failed
# -667 Mysql local connection failed
# -9999 execution is fine
# -300 Mysql execution failed
# -301 Fetch mysql execution failed

# Take tuple or list or 5 elements
@op_fails_repoter(mode="normal", job=G())
def mlogs_mysql_connection(mlogs=None):
    host, port, user, password, with_auto_commit = logs
    try:
        return pymysql.connect(host=host,
                               user=user,
                               password=password,
                               autocommit=with_auto_commit).cursor()
    except:
        return -666

@op_fails_repoter(mode="normal", job=G())
def kwargs_mysql_connection(host=None, port=None, user=None, password=None, with_auto_commit=True):
    try:
        return pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               with_auto_commit=with_auto_commit).cursor()
    return -666

@op_fails_repoter(mode="normal", job=G())
def mysql_local_connection(with_auto_commit=True):
    try:
        return pymysql.connect(host="localhost",
                               user="root",
                               password="uehMLMRw",
                               with_auto_commit=with_auto_commit).cursor()
    return
        return -667

@op_fails_reporter(mode="zilean-op-type", job=G())
def execute_sql(*args, cursor=None):
    try:
        for query in list(args):
            cursor.execute(query)
        return ZileanOp(None, -9999)
    except:
        return ZileanOp(None, -300)

def zilean_sql(*args):
    return execute_sql(*args, cursor=mysql_local_connection())

@op_fails_reporter(mode="zilean-op-type", job=G())
def fetch_sql_result(*args, cursor=None):
    try:
        for query in list(args):
            corsor.execute(query)
        return ZileanOp(cursor.fetchall(), -9999)

    except:
        return ZileanOp(None, -301)

def zilean_fetch_sql(*args):
    return fetch_sql_result(*args, cursor=mysql_local_connection())
