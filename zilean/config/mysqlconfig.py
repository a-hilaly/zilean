from ._mysql_cnf import Cnf
from ._service import Service
from ._storage import StorageDisk


class _MysqlConfig(object):
    """
    MysqlConfig = _MysqlConfig()
    MysqlConfig.Service.start_mysql_service()
    MysqlConfig.Cnf.replace_bind_adress('0.0.0.0')

    """
    def __init__(self):
        self.Storage = StorageDisk
        self.Service = Service
        self.Conf = Cnf


MysqlConfig = _MysqlConfig()
