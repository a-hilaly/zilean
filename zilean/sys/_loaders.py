from zilean.utils.mysql_utils import (table_fields,
                                      select_elements)
from .models.zilean_rtype import _refetch_filter

zilean_db = "zileansystem"
zilean_env = "zilean_env"

def load_zilean_envirenements(mode=None, status="active"):
    if mode:
        return select_elements(zilean_db, zilean_env,
                               selection="*",
                               where="mode = '{0}'".format(mode)).result

    return select_elements(zilean_db, zilean_env,
                           selection="*",
                           where="status = '{0}'".format(status)).result

def load_zilean_active_env():
    pass

def all_zilean_envs():
    pass

def add_zilean_envs():
    pass

def make_zilean_envs():
    pass

def edit_env_config():
    pass

#####################################

def zilean_linked_databases():
    pass

def zilean_unlinked_databases():
    pass

def zilean_link_database():
    pass

def zilean_unlink_database():
    pass

#########################################

def zilean_linked_directories():
    pass

def zilean_link_directory():
    pass

def zilean_unlink_directory():
    pass
