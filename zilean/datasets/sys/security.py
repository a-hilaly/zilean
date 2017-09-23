from greww.data.mysql import MysqlPen as M

UNLOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT UNLOCK;"
LOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT LOCK;"
GRANT_POWER = "GRANT {0} ON {1}.{2} TO '{3}'@'{4}';"
REVOKE_POWER = "REVOKE {0} ON {1}.{2} FROM '{3}'@'{4}';"
USER_RIGHTS = "SHOW GRANTS FOR '{0}'@'{1}';"

def _manage_kwargs_1(grants=None, on_db=None, on_tb=None):
    g = grants
    d = on_db
    t = on_tb
    if grants == "*":
        g = "ALL PRIVILEGES"
    if not on_db:
        d = "*"
    if not on_tb:
        t = "*"
    return g, d, t

class WithGrantsOptions(object):

    @staticmethod
    def set_user_grants(user,
                        host,
                        grants=None,
                        database=None,
                        table=None):
        """
        Grants rights to user
        """
        g, d, t = _manage_kwargs_1(grants, database, table)
        M.execute(GRANT_POWER.format(g,
                                     d,
                                     t,
                                     user,
                                     host))

    @staticmethod
    def revoke_user_grants(user,
                           host,
                           grants=None,
                           database=None,
                           table=None):
        """
        Revoke writes
        """
        g, d, t = _manage_kwargs_1(grants, database, table)
        M.execute(REVOKE_POWER.format(g,
                                      d,
                                      t,
                                      user,
                                      host))

    @staticmethod
    def user_grants(user, host):
        """
        Show User grants
        """
        return M.execute_op(USER_RIGHTS.format(user, host))

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
