from greww.data import MysqlPen as M

UNLOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT UNLOCK;"
LOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT LOCK;"
GRANT_POWER = """GRANT {0} ON {1}.{2} TO '{3}'@'{4}';
FLUSH PRIVILEGES;"""
REVOKE_POWER = """REVOKE {0} ON {1}.{2} FROM '{3}'@'{4}';
FLUSH PRIVILEGES;"""
USER_RIGHTS = "SHOW GRANTS FOR '{0}'@'{1}';"

class WithGrantsOptions(object):

    @staticmethod
    def grants_rights(user,
                      host,
                      grants="ALL",
                      database="*",
                      table="*"):
        """
        Grants rights to user
        """
        M.execute(GRANTS_POWER.format(grants,
                                      database,
                                      table,
                                      user,
                                      host))

    @staticmethod
    def revoke_rights(user,
                      host,
                      rights="ALL",
                      database="*",
                      table="*"):
        """
        Revoke writes
        """
        M.execute(REVOKE_POWER.format(grants,
                                      database,
                                      table,
                                      user,
                                      host))

    @staticmethod
    def show_grants(user, host):
        """
        Show User grants
        """
        M.execute(GRANTS_POWER.format(user, host))


class WithLockOptions(object):

    @staticmethod
    def lock_user(user, host):
        """
        Show User grants
        """
        M.execute(LOCK_USER.format(user, host))

    @staticmethod
    def unlock_user(user, host):
        """
        Show User grants
        """
        M.execute(UNLOCK_USER.format(user, host))
