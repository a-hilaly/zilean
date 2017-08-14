import time
from greww.data import MysqlPen as M
from .zileancache import ZileanCache
from .moves import cachemove

class ZileanBackups(ZileanCache):

    __slots__ = ["_data"]

    table = "zilean_backups_history"
    fields = ["backup_id",
              "targeted_databases",
              "timed_at",
              'working_directory',
              "success"]

    @cachemove(__file__, ZileanBackups)
    def register_backup(self,
                        db=None,
                        workingdir=None,
                        backupfile=None
                        run_time=None,
                        success=None):
        M.add_element(self.db,
                      self.table,
                      database=db,
                      working_directory=workingdir,
                      backup_file=backupfile,
                      run_time=run_time,
                      success=success)

    @classmethod
    def _register_backup(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__()
        obj.register_backup(*args, **kwargs)

def cachebackup(func):
    def wrap_args(*args, **kwargs):
        t1 = time.time()
        try:
            res = func(*args, **kwargs)
            t2 = time.time()
            ZileanBackups._register_backup(**self._filter_kwargs(**kwargs),
                                           run_time=t2-t1,
                                           success=1)
        except:
            ZileanBackups._register_backup(**self._filter_kwargs(**kwargs),
                                           run_time=t2-t1,
                                           success=0)
    return wrap_args
