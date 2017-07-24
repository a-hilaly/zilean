

class ZileanOP(object):
    """
    Zilean out_put type
    as a beta we need to controll all zilean outputs and report em if they fail
    kappa
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
