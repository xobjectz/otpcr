# This file is placed in the Public Domain.


"locks"


import _thread


lock       = _thread.allocate_lock()


def __dir__():
    return (
        'brokerlock',
        'disklock',
        'lock'
    )
