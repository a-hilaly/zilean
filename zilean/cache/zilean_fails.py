from greww.data import MysqlPen as M

def record_zilean_fail(move_id, function, arguments, error_id=None, _type="):
    args = JSON_PYSTR(arguments)

    M.add_element(zilean_cache,
                  zilean_intern_fails,
                  move_id=move_id,
                  type=_type,
                  error_id=error_id,
                  function=function)
