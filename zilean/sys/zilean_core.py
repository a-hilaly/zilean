
def op_fails_reporter(mode=None, job=None):
    pass

def op_moves_reporter():
    pass

def generate_new_job():
    pass

def check_actual_job():
    pass

def update_actual_job():
    pass

def end_actual_job():
    pass

def link_database():
    pass

def unlink_database():
    pass


def intern_fail_reporter():
    # Intern fail repoter
    pass


def zilean():
    pass

def unzilean():
    pass

def unzilean_ifempty():
    pass

def get_job():
    return 1

def incr_subjob():
    pass

def incr_job():
    pass

def set_job():
    pass


# CHECKERS

def check_zilean_system():
    pass

def check_zilean_cache():
    pass


def check_zilean_mysql_dependencies(*targets):
    """
    Checks if zilean mysql databases are correctly installed
    ========================================================
    """
    pass

def make_zilean_dependencies(force=False):
    """
    Run mysql scripts to make zilean databases.
    ========================================================
    """
    pass

def remake_zilean_dependencies(mode="safe"):
    """
    Remove and make zilean mysql databases. Using safe mode
    try to bring back all the previous data.
    ========================================================
    """
    pass

def zilean_config(*targets):
    """
    Return a Dict type representing zilean actual configuration
    ========================================================
    """
    pass

def set_zilean_config(**kwargs):
    """
    Set zilean configuration
    ========================================================
    """
    pass

def zilean_system_config():
    """
    Get zilean system configuration
    ========================================================
    """
    pass

def link_database(database):
    """
    Link database to zilean linked database
    ========================================================
    """
    pass

def unlink_database(database):
    """
    Unlink database from zilean linked database
    ========================================================
    """
    pass

def zilean_status():
    """
    Get zilean actual status
    ========================================================
    """
    pass

def analyse_zilean_success_rates():
    """
    Analyse zilean succes rate
    ========================================================
    """
    pass

def reset_zilean_succes_rate():
    pass

def get_zilean_moves_history():
    pass

def get_zilean_fails_history():
    pass

def get_zilean_jobs_history():
    pass
