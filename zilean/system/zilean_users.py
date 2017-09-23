from zilean.datasets.sys.users import ZileanUsers, ZileanAdmin
from zilean.datasets.sys.machines import ZileanMachines
from zilean._config import ZileanConfig as ZC

class NotAllowedCreation(Exception):
    pass

class NotAllowedDeletion(Exception):
    pass

class NotAllowedPromotion(Exception):
    pass

class NotAllowedDelegation(Exception):
    pass

class VoidArgs(Exception):
    pass

def _manage_kwargs_1(grants=None, on_db=None, on_tb=None):
    g = grants
    d = on_db
    t = on_tb
    if grants == "*":
        g = "ALL"
    if not on_db:
        d = "*"
    if not on_tb:
        t = "*"
    return g, d, t

class ZileanUsers(object):

    users = ZileanUsers
    machines = MachinesData
    admins = ZileanAdmin

    def __init__(self):
        for el, val in ZC.load(self.__class__.__name__).items():
            setattr(self, el, val)

    @classmethod
    def create_user(cls, user, host, password=None, grants=None, on_db=None, on_tb=None):
        obj = object.__new__(cls)
        obj.__init__()
        #
        if not user or not host:
            raise VoidArgs()
        if not 'C' in obj.users_allow:
            raise NotAllowedCreation
        if password is None:
            obj.users.create_user(user, host)
        obj.users.create_user(user, host, password)
        if grants:
            g, d, t = _manage_kwargs_1(grants, on_db, on_tb)
            obj.users.set_user_grants(user, host, g, d, t)

    @classmethod
    def user_grants(cls, user, host):
        cls.users.user_grants(user, host)

    @classmethod
    def set_user_grants(cls, user, host):
        pass

    @classmethod
    def remove_user(cls, user, host):
        cls.users.remove_user(user, host)

    @classmethod
    def create_machine(cls, as_admin=False):
        pass

    @classmethod
    def delete_machine(cls, machine_id=None, machine_name=None, alias=None, adress=None):
        pass

    @classmethod
    def create_admin(cls, user, host, password=None, grants='*'):
        cls.create_user(user, host, password, grants)

    @classmethod
    def remove_admin(cls, user, host):
        cls.users.remove_user(cls, user, host)
