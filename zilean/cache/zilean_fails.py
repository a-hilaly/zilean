

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
