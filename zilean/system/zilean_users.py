from zilean.datasets.sys.users import ZileanUsers
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

class UserDoesntExist(Exception):
    pass

class UserExists(Exception):
    pass

class GrantsLocked(Exception):
    pass

users = ZileanUsers

class ZileanUsers(object):

    def __init__(self):
        for el, val in ZC.load(self.__class__.__name__).items():
            setattr(self, el, val)

    def all_users(self, filter_by=None):
        if filter_by is None:
            return users.users_list()
        return users.users_list(filter_by=filter_by)

    def all_super(self, filter_by=None):
        return users.superuser_list()

    def all_machines():
        pass

    def _check_user(self, user, host):
        if not user or not host:
            raise VoidArgs()
        if (user, host) in users.users_list():
            return True
        return False

    def create_user(self, user, host, password=None, grants=None, on_db=None, on_tb=None):
        if self._check_user(user, host):
            raise UserExists()
        if not 'C' in self.users_allows:
            raise NotAllowedCreation()
        if password is None:
            users.create_user(user, host)
        else:
            users.create_user(user, host, password)
        if grants:
            users.set_user_grants(user, host, grants, on_db, on_tb)

    def remove_user(self, user, host):
        if not self._check_user(user, host):
            raise UserDoesntExist()
        if not 'X' in self.users_allows:
            raise NotAllowedCreation()
        users.remove_user(user, host)

    def user_grants(self, user, host):
        if not self._check_user(user, host):
            raise UserDoesntExist()
        return users.user_grants(user, host)

    def set_user_grants(self, user, host, grants=None, on_db=None, on_tb=None):
        if not self._check_user(user, host):
            raise UserDoesntExist()
        if self.lock_grants == 'true':
            raise GrantsLocked()
        users.set_user_grants(user, host, grants, on_db, on_tb)

    def revoke_user_grants(self, user, host, grants=None, on_db=None, on_tb=None):
        if not self._check_user(user, host):
            raise UserDoesntExist()
        if self.lock_grants == 'true':
            raise GrantsLocked()
        users.revoke_user_grants(user, host, grants, on_db, on_tb)

    def create_machine(self, as_superuser=False):
        pass

    def delete_machine(self, machine_id=None, machine_name=None, alias=None, adress=None):
        pass

    def create_super_user(self, user, host, password=None):
        self.create_user(user, host, password, grants='*')

    def remove_super_user(self, user, host):
        self.remove_user(user, host)
