class ZileanCache(object):
    """
    Zilean Cache Tables Data Manipulation
    """

    __slots__ = ["_data"]

    db = "zileancache"
    table = ""
    fields = []

    def __init__(self):
        """
        Initialise class instance with table content as data
        ====================================================
        """
        self._data = dict(M.table_content(self.db, self.table))

    def update(self):
        """
        Call __init__() in order to rewrite _data attribute
        with the newest table
        ====================================================
        """
        self.__init__()

    @property
    def data(self):
        return self._data

    @classmethod
    def DATA(cls):
        obj = object.__new__(cls)
        obj.__init__()
        return obj._data

    @classmethod
    def _quantify(cls, line=0):
        """
        Return a Dict (Json type) with fields as keys and line
        as values
        =====================================================
        """
        return dict(zip(self.fields, line))
