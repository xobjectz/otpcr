# This file is placed in the Public Domain.


"runtime"


from .broker  import Broker
from .client  import spl
from .scanner import skip


broker = Broker()


def init(pkg, modstr, disable=""):
    "init"
    mds = []
    for modname in spl(modstr):
        if skip(modname, disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        if "init" in dir(module):
            module.init()
            mds.append(module)
    return mds



def __dir__():
    return (
        'init',
        'broker',
    )
