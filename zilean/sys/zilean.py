from ._reporters import (with_new_session_id,
                         with_main_job,


@with_main_job()
@with_new_session_id()
class Zilean(object):
    pass
