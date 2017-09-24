from greww._config import GConfigLoader
from zilean._envs import ZILEAN_CONFIG

__cnf = 'zilean_config'
__f = 'zilean_gconfig.ini'
__type = '__ini__'

def add_zilean_configuration_to_greww():
    path = "{0}/{1}".format(ZILEAN_CONFIG, __f)
    GConfigLoader.add_config(__cnf, path, __type, True)
