from .mysql_query import (_IE_QUERY,
                          JSON_PYSTR,
                          _SELECT_OPTI,
                          _UE_QUERY)
from zilean.sys.models.zilean_rtype import ZileanOP
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

def record_zilean_fail(move_id, function, arguments, error_id=None, _type="intern",):
    args = JSON_PYSTR(arguments)
    if error_id:
        return execute_only(_IE_QUERY(zilean_cache,
                                      zilean_intern_fails,
                                      move_id=move_id,
                                      type=_type,
                                      function=function,
                                      error_id=error_id), commit=True)
    return execute_only(_IE_QUERY(zilean_cache,
                                  zilean_intern_fails,
                                  move_id=move_id,
                                  type=_type,
                                  function=function), commit=True)

def utils_fails_report():
    """
    Not Implemented
    Build will fail if this decorator is defined here due to
    import conflicts
    """
    pass


def kargs(*args, **kwargs):
    return list(args) + list(kwargs.values())

def zilean_reporter(with_time_limit=None,
                    on_fail_only=False,
                    result_checker=lambda x : len(x) != 0,
                    mysql_record=True,
                    ping=False,
                    request=False,
                    op_dir=None):
    #FIXME: Maybe there is a better way to do all this ?
    #       Mmmmmmmmmmmmmayyybeeeee
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            function_name = func.__name__
            arguments = kargs(*args, **kwargs)
            if mysql_record:
                if not on_fail_only:
                    new_zilean_move(function_name, arguments)
                    mv_id = get_last_move_id()
                    try:
                        res = function(*args, **kwargs)
                    except:
                        record_zilean_fail(mv_id,
                                           function_name,
                                           arguments)
                        return -1
                    if isinstance(res, ZileanOP):
                        if res.status > -9000:
                            update_last_move(res.result, 0)
                            record_zilean_fail(mv_id,
                                               function_name,
                                               arguments,
                                               error_id=res.status)
                        else:
                            update_last_move(res.result, 1)
                    else:
                        if not result_checker(res):
                            update_last_move(res, 0)
                            record_zilean_fail(mv_id,
                                               function_name,
                                               arguments,
                                               error_id=-5000)
                        else:
                            update_last_move(res, 1)
                else:
                    raise Exception("Not Implemented")
            else:
                raise Exception("Not Implmented")







        return wrap_args
    return wrap_func
