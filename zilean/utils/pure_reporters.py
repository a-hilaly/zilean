from .mysql_query import (_IE_QUERY,
                          JSON_PYSTR,
                          _SELECT_OPTI,
                          _UE_QUERY)
from .mysql_access import (execute_only,
                           execute_and_fetch)


#XXX: Do not use decorators at .mysql_access and .mysql_query

zilean_cache = "zileancache"
zilean_intern_fails = "zilean_intern_fails"
zilean_moves_history = "zilean_moves_history"

def new_zilean_move(function, arguments):
    args = JSON_PYSTR(arguments)
    return execute_only(_IE_QUERY(zilean_cache,
                        zilean_moves_history,
                        function=function,
                        arguments=args), commit=True)


def get_last_move_id():
    return execute_and_fetch(_SELECT_OPTI.format("move_id",
                                                 zilean_cache,
                                                 zilean_moves_history,
                                                 "move_id",
                                                 "DESC",
                                                 1)).result[0][0]

def update_last_move(out_put, success):
    _move_id = get_last_move_id()
    sets = "`out_put` = '{0}', `success` = {1}".format(JSON_PYSTR(out_put), success)
    return execute_only(_UE_QUERY(zilean_cache,
                                  zilean_moves_history,
                                  "move_id = {0}".format(_move_id),
                                  1,
                                  sets), commit=True)

def record_zilean_fail(function, error_id, arguments, _type="intern", move_id=None):
    pass

def utils_fails_report():
    """
    Not Implemented
    Build will fail if this decorator is defined here due to
    import conflicts
    """
    pass


def zilean_reporter(intern=True,
                    only_if_fails=False,
                    raise_on_warnings=False,
                    zilean_type=False,
                    ping=False,
                    redirect=None):

    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            pass
        return wrap_args
    return wrap_func
