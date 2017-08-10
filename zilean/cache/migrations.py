from greww.data import MysqlPen
from .zileancache import ZileanCache
from .moves import cachemove

class ZileanMigrations(ZileanCache):

    __slots__ = ["_data"]

    table = "zilean_backups_history"
    fields = ["backup_id",
              "targeted_databases",
              "timed_at",
              'working_directory',
              "success"]

    @cachemove(__file__, ZileanBackups.__name__)
    def register_migration(self,
                           db=None,
                           backupfile=None,
                           run_time=None,
                           success=None):
        M.add_element(self.db,
                      self.table,
                      database=db,
                      backup_file=backupfile,
                      run_time=run_time,
                      success=success)

    @classmethod
    def _register_backup(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__()
        obj.register_move(*args, **kwargs)
