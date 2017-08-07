from ._loaders import (load_zilean_envirenements,
                       edit_env_config)

def assert_zilean_session(session_owner=None, session_id=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            pass

class ZileanEnvirenement(object):
    __slots__ = ['_mode',
                 'status',
                 'working_directory',
                 'mysql_connector_use_pure',
                 'recording_sessions',
                 'recording_pen_history'
                 'recording_fails',
                 'max_runtime_before_fail',
                 'recording_db_backups',
                 'recording_dr_backups',
                 'default_backup_type']

    def __init__(self):
        kwargs = self._load_env_as_dict()
        for kw, val in kwargs.items():
            setattr(self, kw, val)

    def __call__(self):
        self.__init__()

    def __str__(self):
        return "Zilean-mode : {0}".format(self.mode)

    __repr__ = __str__

    #@assert_zilean_session("zilean")
    def remake_zilean_envirement(self):
        from zilean.zilean_maker import make_zilean_envirement
        make_zilean_envirement(force=True)
        self.__init__()

    @classmethod
    def _load_env_as_dict(cls):
        envs = load_zilean_envirenements()
        return dict(zip(cls.__slots__, envs[0]))

    @property
    def mode(self):
        return self._mode

    @property
    def active(self):
        return self.status == 'active'

    def set_config(self, target, value):
        edit_env_config(self.mode, target, value)
        setattr(self, target, value)

    def assert_config(self, config):
        pass

    def assert_all_configurations(self):
        pass

    def deactivate_mode(self, mode=None):
        pass

    def activate_mode(self, mode=None):
        pass

    @staticmethod
    def count_activated_modes():
        pass

    def solve_modes_activation_conflicts(self):
        pass

    def new_mode(self):
        pass

    def delete_mode(self):
        pass




#XXX: @zilean_env_config(function_check=lambda x : x != None)
def zilean_env_config(function_check=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            pass
    pass
