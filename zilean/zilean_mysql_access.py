import pymysql.cursors



# Take tuple or list or 5 elements
def mlogs_mysql_connection(mlogs=None):
    host, port, user, password, with_auto_commit = logs
    try:
        return pymysql.connect(host=host,
                               user=user,
                               password=password,
                               autocommit=with_auto_commit).cursor()
    except:
        import time
        return -666

# kwargs
def kwargs_mysql_connection(host=None, port=None, user=None, password=None, with_auto_commit=True):
    try:
        return pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               with_auto_commit=with_auto_commit).cursor()
    return -666

def mysql_local_connection(with_auto_commit=True):
    try:
        return pymysql.connect(host="localhost",
                               user="root",
                               password="uehMLMRw",
                               with_auto_commit=with_auto_commit).cursor()
    return
        return -667


def execute_sql(*args, cursor=None):
    try:
        for query in list(args):
            cursor.execute(query)
        return -9999
    except:
        return -300

def zilean_sql(*args):
    return execute_sql(*args, cursor=mysql_local_connection())

def fetch_sql_result(*args, cursor=mysql_local_connection()):
    try:
        for query in list(args):
            corsor.execute(query)
        return cursor.fetchall()
    except:
        return -301

def zilean_fetch_sql(*args):
    return fetch_sql_result(*args, cursor=mysql_local_connection())
