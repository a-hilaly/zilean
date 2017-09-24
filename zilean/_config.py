from greww.data.config import option_data, configuration_data
from greww._config import GrewwConfig, Configuration
from ._envs import ZILEAN_CONFIG


class ZileanConfig(object):

    path = ZILEAN_CONFIG

    @classmethod
    def load(cls, c):
        return configuration_data(cls.path, c)

    @classmethod
    def load_option(cls, c, o):
        return option_data(cls.path, c, o)
