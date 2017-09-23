from greww.data import MysqlPen as M
from zilean.datasetts.basics import BasicTable

class ZLinkedDatabases(BasicTable):

    __slots__ = ["data"]

    table = "zilean_linked_databases"
    fields = ['database_id',
              'database',
              'linked_time',
              'last_backup_id',
              'last_backup_time']

    @classmethod
    def is_linked(cls, db):
        obj = object.__new__(cls)
        obj.__init__()
        for line in obj._data:
            if line[1] == db:
                return True
        return False

    @classmethod
    def all_linked(cls, filter_by=['database']):
        return cls.DATA()


    @classmethod
    def linked_database_data(cls, db):
        obj = object.__new__(cls)
        obj.__init__()
        for line in obj.data:
            if line[1] == db:
                return line
        raise DatabaseDataError(db)


    @classmethod
    def link_database(cls, db):
        M.add_element(cls.db,
                      cls.table,
                      database=db)

    @classmethod
    def delink_database(cls, db):
        M.remove_elements(cls.db,
                          self.table,
                          where="database = '{0}'".format(db))

    @classmethod
    def database_last_n_backups(cls, db):
        pass

    @classmethod
    def register_database_backup(cls, backup_id, db=None, database_id=None):
        pass
