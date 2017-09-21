from greww.data import MysqlPen as M
from zilean.data.basics import ZileanCache
from zilean.data.cache import ZileanMoves

class DatabaseDataError(Exception):
    pass

class LinkedDatabasesData(ZileanSys):

    __slots__ = ["data"]

    table = "zilean_linked_databases"
    fields = ['database_id',
              'database',
              'local',
              'linked_time',
              'last_backup_id']

    @zileanmoves(__file__, LinkedDatabasesData)
    def islinked(self, db):
        for line in self._data:
            if line[1] == db:
                return True
        return False

    @zileanmoves(__file__, LinkedDatabasesData)
    def database_data(self, db):
        for line in self.data:
            if line[1] == db:
                return line
        raise DatabaseDataError(db)

    @zileanmoves(__file__, LinkedDatabasesData)
    def link_database(self, db, local=True):
        l = 1 if local else 0
        M.add_element(self.db,
                      self.table,
                      database=db,
                      local=l)

    @zileanmoves(__file__, LinkedDatabasesData)
    def delink_database(self, db):
        M.remove_elements(self.db,
                          self.table,
                          where="database = '{0}'".format(db))

    @classmethod
    def _islinked(cls, db):
        obj = object.__new__(cls)
        obj = obj.__init__()
        return obj.islinked(db)

    @classmethod
    def _database_data(cls, db):
        obj = object.__new__(cls)
        obj = obj.__init__()
        return obj.database_data(db)

    @classmethod
    def _link_database(cls, db, local=True):
        obj = object.__new__(cls)
        return obj.link_database(db, local=local)

    @classmethod
    def _delink_database(cls, db):
        obj = object.__new__(cls)
        return obj.link_database(db, local=local)
