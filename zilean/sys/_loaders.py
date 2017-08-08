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
