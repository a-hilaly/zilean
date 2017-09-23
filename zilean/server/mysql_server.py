from .conf._mysqld_cnf import Cnf
from .conf._service import Service
from .conf._storage import StorageDisk


class _MysqlServer(object):
    """
    MysqlConfig = _MysqlConfig()
    MysqlConfig.Service.start_mysql_service()
    MysqlConfig.Cnf.replace_bind_adress('0.0.0.0')
    """
    def __init__(self):
        self.Storage = StorageDisk
        self.Service = Service
        self.Conf = Cnf

MysqlServer = _MysqlServer()
