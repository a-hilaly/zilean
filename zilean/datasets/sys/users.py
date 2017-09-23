#from zilean.core._envs import zilean_pkg_config
from zilean.data.basics import BasicTable
from .security import WithGrantsOptions, WithLockOptions
#
ADD_USER = "CREATE USER '{0}'@'{1}' IDENTIFIED BY '{2}';"

_DEFAULT_PASSWORD = "1" #zilean_pkg_config("DEFAULT", "default_password")

class ZileanUsers(BasicTable, WithGrantsOptions, WithLockOptions):

    db = "mysql"
    table = "user"
    fields = []

    def __init__(self):
        BasicTable.__init__(self)

    # +/- User

    @staticmethod
    def create_user(user, host, password=_DEFAULT_PASSWORD):
        """
        Add User to mysql server configuration
        """
        pass

    @staticmethod
    def remove_user(use, host):
        """
        Remove User from mysql server configuration
        """
        pass

    @classmethod
    def users_list(cls, *args, filtered_by=['User', 'Host']):
        """
        Return list of users filtred by filtred_by + *args
        """
        pass

    @staticmethod
    def user_grants(user, host):
        """
        Return user Grants
        """
        pass

    @staticmethod
    def set_user_grants(user,
                        host,
                        grants=None,
                        db=None,
                        table=None):
        """
        Set user grants at db.table
        """
        pass

    @staticmethod
    def remove_user_grants(cls,
                           user,
                           host,
                           grants=None,
                           db=None,
                           table=None):
        """
        Remove user grants at db.table
        """
        pass

    @classmethod
    def _compare_users_to_registred_machines(cls):
        pass


class ZileanAdmins(ZileanUsers):

    @classmethod
    def create_admin(cls, *args, **kwargs):
        pass

    @classmethod
    def admins_list(cls):
        pass

    @classmethod
    def remove_admin(cls):
        pass