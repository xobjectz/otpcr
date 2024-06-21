# This file is placed in the Public Doman.


"utilities"


import pathlib


def cdir(pth):
    "create directory."
    path = pathlib.Path(pth)
    path.parent.mkdir(parents=True, exist_ok=True)


def __dir__():
    return (
        'cdir',
    )
