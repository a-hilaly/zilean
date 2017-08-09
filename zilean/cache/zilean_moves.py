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
                                                 1))

def update_last_move(out_put, success):
    _move_id = get_last_move_id()
    sets = "`out_put` = '{0}', `success` = {1}".format(JSON_PYSTR(out_put), success)
    return execute_only(_UE_QUERY(zilean_cache,
                                  zilean_moves_history,
                                  "move_id = {0}".format(_move_id),
                                  1,
                                  sets), commit=True)
