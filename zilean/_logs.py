import os
from greww.utils import ConfParser
from greww.env import MachineEnvirenement as ME


config_file_path = ME.import_var("ZILEAN_MACHINE_CONFIG")
zilean_config = ConfParser.(config_file_path)


ZILEAN_CONFIG = zilean_config["zilean.config"]
MYSQL_LOGS = zilean_config["mysql.logs"]
MYSQL_CONFIG = zilean_config["mysql.config"]
