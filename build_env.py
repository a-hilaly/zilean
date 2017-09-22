import os
import skmvs as SK

ZP = os.environ['ZILEAN_PATH']
ZS = "{0}/scripts".format(ZP)
ZAPI = "{0}/api".formar(ZP)
ZV = os.environ['ZILEAN_VERSION']

def build():
    SK.store_value("ZILEAN_PATH", ZP, db='paths', force=True)
    SK.store_value("ZILEAN_SCRIPTS", ZS, db='paths', force=True)
    SK.store_value("ZILEAN_API", ZAPI, db='paths', force=True)
    SK.store_value("ZILEAN_VERSION", ZV, db='main', force=True)
    SK.store_value("zilean_paths_stored", True, db='main', force=True)

def make():
    build()

if __name__ == "__main__":
    make()
