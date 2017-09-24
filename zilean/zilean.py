


class Zilean(object):

    def __new__(cls):
        obj = object.__new__(cls)
        obj.__init__()
        obj.Builder.check_system()
        return obj

    def __init__(self):
        self._init_configs()
        self.server_status = 0
        self.zilean_status = 0

    def _init_configs(self):
        self.Migrator.__init__()
        self.Backuper.__init__()
        self.Builder.__init__()
        self.Partitions.__init__()
        self.Users.__init__()
        self.Config.__init__()
        self.Server.__init__()
        self.Env.__init__()

    def _init_envs():
        pass

    def _make_configs():
        pass

    def _load_configs():
        pass

    def _check_system():
        pass

    def _solve_system_errors():
        pass

    def _make_zilean_system():
        pass
