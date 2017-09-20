import time
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

    @cachemove(__file__, ZileanMigrations)
    def _register_migration(self,
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
    def register_migration(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__()
        obj.register_migration(*args, **kwargs)

    @classmethod
    def clear_cache(clear):
        pass

def _filter_kwargs(**kwargs):
    pass

#FIXME
def cachemigration(func):
    def wrap_args(*args, **kwargs):
        t1 = time.time()
        try:
            res = func(*args, **kwargs)
            t2 = time.time()
            ZileanMigrations.register_migration(**_filter_kwargs(**kwargs),
                                                run_time=t2-t1,
                                                success=1)
        except:
            ZileanMigrations.register_migration(**_filter_kwargs(**kwargs),
                                                run_time=t2-t1,
                                                success=0)
    return wrap_args
