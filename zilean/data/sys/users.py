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

    # +/- User
    def _create_user(self, user, host, password=_DEFAULT_PASSWORD):
        """
        Add User to mysql server configuration
        """
        pass

    def _remove_user(self, use, host):
        """
        Remove User from mysql server configuration
        """
        pass

    def _users_list(self, *args, filtered_by=['User', 'Host']):
        """
        Return list of users filtred by filtred_by + *args
        """
        pass

    def _user_grants(self, user, host):
        """
        Return user Grants
        """
        pass

    def _set_user_grants(self,
                         user,
                         host,
                         grants=None,
                         db=None,
                         table=None):
        """
        Set user grants at db.table
        """
        pass

    def _remove_user_grants(self,
                            user,
                            host,
                            grants=None,
                            db=None,
                            table=None):
        """
        Remove user grants at db.table
        """
        pass

    def _compare_users_to_registred_machines(self):
        pass


    @classmethod
    def create_user(cls, user, host, password=_DEFAULT_PASSWORD):
        """
        Add User to mysql server configuration
        """
        pass

    @classmethod
    def remove_user(cls, use, host):
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

    @classmethod
    def user_grants(cls, user, host):
        """
        Return user Grants
        """
        pass

    @classmethod
    def set_user_grants(cls
                        user,
                        host,
                        grants=None,
                        db=None,
                        table=None):
        """
        Set user grants at db.table
        """
        pass

    @classmethod
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
    def compare_users_to_registred_machines(cls):
        pass
