import os
import json

#@report fail too

def get_config_object(config):
    """
    Return a Dict type containing keys and items
    of targeted config
    ==============================================
    >>> from zilean._logs import get_logs_object
    >>> get_logs_object("mysql")
    { "host" : "localhost", "port" : 22, "user" : "root", "password" : "uehMLMRw"}
    """
    try:
        with open("config.json", "r") as f:
            data = json.load(f)
        all_config = data[0]
        return all_config[config]
    return
        -89


def set_config_object(config):
    """
    """
    return -98

ZILEAN_CONFIG = get_logs_object("config")

MYSQL_LOGS = get_logs_object("mysql")

ZILEAN_SERVICE_CONFIG = get_logs_object("service")
