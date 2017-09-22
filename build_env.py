import os
import skmvs as SK

ZP = os.environ['ZILEAN_PATH']
ZS = os.environ['ZILEAN_SCRIPTS']
ZA = os.environ['ZILEAN_API']
ZV = os.environ['ZILEAN_VERSION']
ZO = os.environ['ZILEAN_OFFICE']

def build():
    SK.store_value("ZILEAN_PATH", ZP, db='paths', force=True)
    SK.store_value("ZILEAN_SCRIPTS", ZS, db='paths', force=True)
    SK.store_value("ZILEAN_API", ZA, db='paths', force=True)
    SK.store_value("ZILEAN_VERSION", ZV, db='main', force=True)
    SK.store_value("ZILEAN_OFFICE", ZV, db='paths', force=True)
    SK.store_value("zilean_paths_stored", True, db='main', force=True)

def make():
    build()

if __name__ == "__main__":
    make()
