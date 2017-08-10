

class ZileanSys(object):
    """
    Zilean System Tables Data Extraction
    """

    __slots__ = ["_data"]

    db = "zileansys"
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
