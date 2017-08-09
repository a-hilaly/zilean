


class _register_database(object):
    def __init__(self, database=None):
        if database is None:
            raise Exception("NaN-")
        fast_dump("zilean_", "zilean_", database=database)


class SimpleDatabase(_register_database):
    def __init__(self, database=None):
        super(self, _register_database).__init__(database=None)


class _db_withtable(object):
    def __init__(self, database=None, **kwargs):
        if database is None:
            raise Exception("NaN-")
        fast_dump("zilean_", "zilean_", database=database)


class OptimisedDatabase(SimpleDatabase):
    pass


class ServerDatabase():
    pass


class OptimisedServerDatabase():
    pass
