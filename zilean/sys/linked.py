from greww.data import MysqlPen as M
from ._exceptions import DatabaseDataError
from .zileansys import ZileanSys

class LinkedDatabasesData(ZileanSys):

    __slots__ = ["data"]

    table = "zilean_linked_databases"
    fields = ['database_id',
              'database',
              'local',
              'linked_time',
              'last_backup_id']

    def islinked(self, db):
        for line in self._data:
            if line[1] == db:
                return True
        return False

    def database_data(self, db):
        for line in self.data:
            if line[1] == db:
                return line
        raise DatabaseDataError(db)

    def link_database(self, db, local=True):
        l = 1 is local else 0
        M.add_element(self.db,
                      self.table,
                      database=db,
                      local=l)

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
