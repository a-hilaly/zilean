from greww.data import MysqlPen as M
from .zileansys import ZileanSys
from ._exceptions import MachineDataError

class MachinesData(ZileanSys):

        __slots__ = ["_data"]

        table = "zilean_registred_machines"
        fields = ['machine_id',
                  'machine_name',
                  'owner',
                  'alias',
                  'extra',
                  'adress',
                  'type',
                  'authorisation',
                  'front_database',
                  'zilean_auto_backup']

        def isregistred(self, machine_name=None, machine_id=None, alias=None):
            for line in self._data.items():
                if machine_id and line[0] == machine_id:
                    return True
                elif machine_name and line[1] == machine_name
                    return True
                elif alias and alias in line[3]:
                    return True
            return False

        def machine_data(self, machine_name=None, machine_id=None, alias=None):
            for line in self._data.items():
                if machine_id and line[0] == machine_id:
                    return dict(zip(self.fields, line)
                elif machine_name and line[1] == machine_name
                    return dict(zip(self.fields, line)
                elif alias and alias in line[3]:
                    return dict(zip(self.fields, line)
            raise MachineDataError(machine_name, machine_id, alias)

        def new_machine(self, **kwargs):
            M.add_element(self.db,
                          self.table,
                          **kwargs)

        def delete_machine(self, machine_name=None, machine_id=None):
            if machine_id:
                M.remove_elements(self.db,
                                  self.table,
                                  where="machine_id = {0}".format(machine_id))
            if machine_name:
                M.remove_elements(self.db,
                                  self.table,
                                  where="machine_name = '{0}".format(machine_name))

        def set_machine_data(self, machine_name=None, machine_id=None, config=None, value=None):
            if machine_name:
                M.update_element(self.db,
                                 self.table,
                                 where="machine_name = '{0}".format(machine_name),
                                 sets="{0} = {1}")
            if machine_id:
                M.update_element(self.db,
                                 self.table,
                                 where="machine_id = '{0}".format(machine_id),
                                 sets="{0} = {1}")

        @classmethod
        def _isregistered(cls, **kwargs):
            obj = object.__new__(cls)
            obj.__init__()
            return obj.isregistred(**kwargs)

        @classmethod
        def _machine_data(cls, **kwargs):
            obj = object.__new__(cls)
            obj.__init__()
            return obj.machine(**kwargs)

        @classmethod
        def _new_machine(cls, **kwargs):
            obj = object.__new__(cls)
            obj.new_machine(**kwargs)

        def _delete_machine(self, **kwargs):
            obj = object.__new__(cls)
            obj.delete_machine(**kwargs)

        def _set_machine_data(cls, **kwargs):
            obj = object.__new__(cls)
            obj.set_machine_data(**kwargs)
