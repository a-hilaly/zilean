

# -666 Mysql connection failed
# -667 Mysql local connection failed
# -9999 execution is fine
# -300 Mysql execution failed
# -301 Fetch mysql execution failed

def record_if_fails(mode="", job=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            if job == "subjob":
                incr_subjob()
            else:
                incr_job()
            job = get_job()
            res = func(*args, **kwargs)
            t = time.ctime()
            if isinstance(res, ZileanOP):
                if res.status > -9000:
                    report_fail(func, job, t, res.status, res.out_put, args=args, kwargs=kwargs)
            return res
        return wrap_args
    return wrap_func


def with_new_session_id():
    pass


def record_move():
    pass


def record_backup():
    pass
