
def load_zilean_env():
    pass

def all_zilean_envs():
    pass

def add_zilean_envs():
    pass

def make_zilean_envs():
    pass


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

    def set_env():
        pass

    def set_zilean_env():
        pass

    def change_zilean_env():
        pass

    def fetch():
        pass


#####################################


def zilean_linked_databases():
    pass



def zilean_unlinked_databases():
    pass
