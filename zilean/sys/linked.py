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

    def link_database(self, db):
        pass

    def delink_database(self, db):
        pass

    @classmethod
    def _islinked(cls, db):
        obj = object.__new__(cls)
        obj = obj.__init__()
        return obj.islinked(db)

    @classmethod
    def _database_data(db):
        obj = object.__new__(cls)
        obj = obj.__init__()
        return obj.database_data(db)

    @classmethod
    def _link_database():
        pass

    @classmethod
    def _delink_database():
        pass
