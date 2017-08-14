import time
from greww.data import MysqlPen as M
from .zileancache import ZileanCache

class ZileanMoves(ZileanCache):

    __slots__ = ["_data"]

    table = "zilean_moves_history"
    fields = ["move_id",
              "timed_at",
              "module",
              "class",
              "function",
              "arguments",
              "output",
              "run_time",
              "success"]

    @cachemove(__file__, ZileanMoves)
    def register_move(self,
                      module=None,
                      _class=None,
                      func=None,
                      args=None,
                      out_put=None,
                      run_time=None,
                      success=None):

        M.add_element(self.db,
                      self.table,
                      module=module,
                      class=_class,
                      arguments=args,
                      out_put=out_put,
                      run_time=run_time,
                      success=success)

    @classmethod
    def _register_move(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.register_move(*args, **kwargs)

def cachemove(module=None, _class=None):
    """
    Decorator to zilean intern function except .zileancache
    """
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            t1 = time.time()
            try:
                res = func(*args, **kwargs)
                t2 = time.time()
                ZileanMoves.register_move(module=module,
                                          _class=_class.__name__,
                                          func=func.__name__,
                                          args=args,
                                          out_put=res,
                                          run_time=t2-t1,
                                          success=1)
            except:
                t2 = time.time()
                ZileanMoves.register_move(module=module,
                                          _class=_class.__name__,
                                          func=func.__name__,
                                          args=args,
                                          run_time=t2-t1,
                                          success=0)
        return wrap_args
    return wrap_func
