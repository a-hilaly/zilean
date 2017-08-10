

class ZileanCache(object):
    """
    Zilean Cache Tables Data Manipulation
    """

    __slots__ = ["_data"]

    db = "zileancache"
    table = ""
    fields = []

    def __init__(self):
        self._data = dict(M.table_content(self.db, self.table))

    def update(self):
        self.__init__()

    @property
    def data(self):
        return self._data

    @classmethod
    def _quantify(cls, line):
        return dict(zip(self.fields, line))
