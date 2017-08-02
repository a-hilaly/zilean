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
        self.out_put = "" if result is None else result
        self.exit_status = status

    def __call__(self):
        return self.__dict__

    def __str__(self):
        if self.status < -9000:
            return "Zilean successed with : {0}".format(self.status)
        return "Zilean failed with : {0}".format(self.status)

    __repr__ = __str__

    @property
    def status(self):
        return self.exit_status

    @status.setter
    def status(self, s):
        self.exit_status = s

    @property
    def result(self):
        return self.out_put

    @result.setter
    def result(self, r):
        self.out_put = r


def tuplik(*args):
    a = list(args)
    if len(a) == 1:
        return a
    return tuple(a)

def _refetch_filter(indexes):
    """
    Decorator to functions that out put a ZileanOP to
    reselect mostly mysql tuple out_puts in result list
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
            ress = []
            try:
                for i in res.result:
                    ress += tuplik(*[i[j] for j in indexes])
                    res.result, res.status = ress, -9998
                return res
            except:
                res.status = -8
                return res
        return wrap_args
    return wrap_func
