#


def check_zilean_dependencies():
    pass

def make_zilean_dependencies():
    pass

def zilean_session_cache():
    pass

def link_database(database):
    pass

def unlink_database(database):
    pass

def zilean_status():
    pass

def report_fail():
    pass

def analyse_zilean_success_rates():
    pass



class ZileanSession(object):
    def __init__(self):
        self.args = zilean_session_cache()
        self.status()

    def _make(self):
        pass

    @property
    def status(self):
        pass

    def link_database(self, database=None):
        pass

    @property
    def linked_databases(self):
        pass

    @property
    def unlinked_databases(self):
        pass

    @property
    def records(self):
        pass

    @property
    def fails(self):
        pass

    @property
    def success_rate():
        pass

    @property
    def history():
        pass

    def reset_success_rate():
        pass

    def generate_database_backup():
        pass

    def make_backup_database():
        pass

    def generate_backups():
        pass

    def make_backups():
        pass

    def _reset_all():
        pass
