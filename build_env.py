import os
import skmvs as SK

#TODO: REDO
ZP = os.getcwd()
ZS = "{0}/scripts".format(ZP)
ZV = "0.0.1"

def _record_var_envs():
    SK.store_value("ZILEAN_PATH", ZP)
    SK.get_value("ZILEAN_SCRIPTS", ZS)
    ZILEAN_VERSION = SK.get_value("ZILEAN_VERSION", ZV)

def make():
    _record_var_envs()


if __name__ == "__main__":
    make()
