from ._loaders import load_zilean_env

class ZileanEnvirenements(object):
    __slots__ = ['mode',
                 'status',
                 'working_directory',
                 'mysql_connector_use_pure',
                 'recording_sessions',
                 'recording_fails',
                 'recording_db_backups',
                 'recording_dr_backups',
                 'default_backup_type']

    def __init__(self):
        envs = load_zilean_env("active")
        for kw, val in envs.items():
            setattr(self, kw, val)

    def __call__(self):
        pass

    @property
    def mode(self):
        pass

    @mode.setter
    def mode(self, new_mode):
        pass

    def set_env():
        pass

    def set_zilean_env():
        pass

    def change_zilean_env():
        pass

    def fetch():
        pass


def _zileanenvirenements():
    pass
