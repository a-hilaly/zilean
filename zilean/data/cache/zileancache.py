from zilean.data.basics import BasicTable

class ZileanCache(object):
    """
    Zilean Cache Tables
    """
    __slots__ = ["_data"]

    db = "zileancache"
    table = ""
    fields = []
