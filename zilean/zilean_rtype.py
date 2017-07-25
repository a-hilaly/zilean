class ZileanOP(object):
    """
    Zilean out_put type
    as a beta we need to controll all zilean outputs
    and reportem if they fail. Kappa
    =================================================
    >>> from zilean import ZileanOP
    >>> output = ZileanOP("data1_test", -9999)
    >>> output()
    { result : "data1_test", exit_status : -9999}
    >>> output.status
    -9999
    >>> output.result
    "data1_test"
    ================================================
    """
    def __init__(self, result=None, status=0):
        self.result = "" if result is None else result
        self.exit_status = status

    def __call__(self):
        return self.__dict__

    @property
    def status(self):
        return self.exit_status

    @property
    def out_put(self):
        return self.result


def _refetch_filter(indexes):
    """
    Decorator to functions that out put a ZileanOP type
    With a list a result
    ===================================================
    >>> f = lambda n: [ZileanOP((x, x+1, x+2), -9999)\
                       for x in range(n)]
    >>> f(2).
    [(0, 1, 2), (1, 2, 3)]
    >>> nf = _refetch_filter([0, 2])f(2)
    [(0, 2), (1, 3)]
    ====================================================
    """
    def wrap_func(func):
        if not indexes:
            return func
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                ress = []
                for i in indexes:
                    ress += res[i]
                return ress
            except:
                return res
        return wrap_args
    return wrap_func
