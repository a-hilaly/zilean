from zilean.datasets.sys.machines import ZileanMachines
from zilean.datasets.sys.linked import ZLinkedDatabases
from .zilean_users import ZileanUsers


class Partition(object):

    def __init__(self, mn, *args):
        self.front = '{0}_zdb'.format(mn)
        self.other = list(args)

    def dump(self):
        r = self.other + [self.front]
        return r

class ZileanPartition(object):

    def __init__(object):
        pass

    def all_partitions(self):
        pass

    def all_databases(self):
        pass

    def all_linked(self):
        pass

    def new_database(self):
        pass

    def remove_database(self):
        pass

    def link_database(self):
        pass

    def add_machine_database(self):
        pass

    def remove_machine_database(self):
        pass

    def machine_partitions(self):
        pass

    def is_partition_of(self):
        pass

    def check_machine_partitions(self):
        pass

    def make_machine_partitions(self):
        pass

    def remove_machine_partitions(self):
        pass
