from greww.data import MysqlPen as M
from .zileansys import ZileanSys
from ._exceptions import ServiceDataError
from zilean.data.cache import zileanmoves


class ServiceData(ZileanSys):

    __slots__ = ["_data"]

    table = "zilean_service"
    fields = ['service', 'status']

    @zileanmoves(__file__, ServiceData)
    def isiservice(self, srvc):
        for service, state in self._data.items():
            if service == srvc:
                return True
        retrun False

    @zileanmoves(__file__, ServiceData)
    def service_status(self, srvc):
        for service, state in self._data.items():
            if service == srvc:
                return state
        raise ServiceDataError(srvc)

    @zileanmoves(__file__, ServiceData)
    def switch_service_status(self, srvc, status=None):
        for service, state in self._data.items():
            if service == srvc:
                if status:
                    ns = status
                else:
                    ns = 0 if state = 1 else 1
                sets = "status = {0}".format(ns)
                where = "service = '{0}'".format(service)
                M.update_element(self.db,
                                 self.table,
                                 where=where
                                 sets=sets)
        raise ServiceDataError(srvc)

    @zileanmoves(__file__, ServiceData)
    def new_service(self, service):
        M.add_element(self.db,
                      self.table,
                      service=service)

    @zileanmoves(__file__, ServiceData)
    def delete_service(self, service):
        M.remove_elements(self.db,
                          self.table,
                          where="service = '{0}'".format(service))
    @classmethod
    def _isservice(cls, service):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.isservice(service)

    @classmethod
    def _service_status(cls, service):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.service_status(service)

    @classmethod
    def _switch_service_status(cls, service, status=None):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.switch_service_status(service, status=status)

    @classmethod
    def _new_service(cls, service):
        obj = object.__new__(cls)
        obj.new_service(service)

    @classmethod
    def _delete_service(self, service):
        obj = object.__new__(cls)
        obj.delete_service(service)
