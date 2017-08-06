from .mysql_query import (_IE_QUERY,
                          JSON_PYSTR,
                          _SELECT_OPTI,
                          _UE_QUERY)
from .mysql_access import execute_only

zilean_cache = "zileancache"
zilean_intern_fails = "zilean_intern_fails"
zilean_moves_history = "zilean_moves_history"

def new_zilean_move(function, arguments):
    args = JSON_PYSTR(arguments)
    print(_IE_QUERY(zilean_cache,
                    zilean_moves_history,
                    function=function,
                    arguments=args))

def get_last_move_id():
    return execute_and_fetch(_SELECT_OPTI.format("move_id",
                                                 db,
                                                 table,
                                                 "move_id",
                                                 "DESC",
                                                 1)).result

def update_last_move(out_put, success):
    _move_id = get_last_move_id()
    sets = "out_put = {0}, success = {1}".format(out_put, success)
    return execute_only(_UE_QUERY(zilean_cache,
                                  zilean_intern_fails,
                                  "move_id = {0}".format(_move_id),
                                  1,
                                  sets))

def record_zilean_fail(function, error_id, arguments, _type="intern", move_id=None):
    pass

def utils_fails_report():
    """
    Not Implemented
    Build will fail if this decorator is defined here due to
    import conflicts
    """
    pass


def zilean_reporter(pure=False,
                    intern=True,
                    only_if_fails=False,
                    raise_on_warnings=False,
                    zilean_type=False):

    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            pass
        return wrap_args
    return wrap_func
