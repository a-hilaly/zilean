from greww.data import MysqlPen as M
from greww.utils.filters import refetch_filter
from zilean.datasets.basics import BasicTable

class MachineDataError(Exception):
    pass

class MachineExists(Exception):
    pass

class MachineDoesntExist(Exception):
    pass

class ZileanMachines(BasicTable):

        __slots__ = ["_data"]

        table = "zilean_registred_machines"
        fields = ['machine_id',
                  'machine_name',
                  'host',
                  'owner',
                  'alias',
                  'extra',
                  'type',
                  'front_database',
                  'other_databases',
                  'zilean_auto_backup']

        @refetch_filter([1])
        @classmethod
        def machines_list(cls):
            obj = object.__new__(cls)
            obj.__init__()
            return obj.data

        @classmethod
        def isregistred(cls, machine_name=None, machine_id=None):
            obj = object.__new__(cls)
            obj.__init__()
            for line in obj._data:
                if machine_id and line[0] == machine_id:
                    return True
                elif machine_name and line[1] == machine_name:
                    return True
                elif alias and alias in line[3]:
                    return True
            return False

        @classmethod
        def machine_data(cls, machine_name=None, machine_id=None):
            obj = object.__new__(cls)
            obj.__init__()
            for line in obj._data:
                if machine_id and line[0] == machine_id:
                    return dict(zip(cls.fields, line))
                elif machine_name and line[1] == machine_name:
                    return dict(zip(cls.fields, line))
                elif alias and alias in line[3]:
                    return dict(zip(cls.fields, line))
            raise MachineDataError(machine_name, machine_id, alias)

        @classmethod
        def new_machine(cls, **kwargs):
            M.add_element(cls.db,
                          cls.table,
                          **kwargs)

        @classmethod
        def delete_machine(cls, machine_name=None, machine_id=None):
            if machine_id:
                M.remove_elements(cls.db,
                                  cls.table,
                                  where="machine_id = {0}".format(machine_id))
            if machine_name:
                M.remove_elements(cls.db,
                                  cls.table,
                                  where="machine_name = '{0}".format(machine_name))

        @classmethod
        def set_machine_data(cls, machine_name=None, machine_id=None, config=None, value=None):
            if machine_name:
                M.update_element(cls.db,
                                 cls.table,
                                 where="machine_name = '{0}".format(machine_name),
                                 sets="{0} = {1}".format(config, value))
            if machine_id:
                M.update_element(cls.db,
                                 cls.table,
                                 where="machine_id = '{0}".format(machine_id),
                                 sets="{0} = {1}".format(config, value))

        @classmethod
        def add_machine_database(cls):
            pass

        @classmethod
        def remove_machine_database(cls):
            pass

        @classmethod
        def make_mysql_config_conf():
            pass
