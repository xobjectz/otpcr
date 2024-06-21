# This file is placed in the Public Domain.
#
# pylint: disable=W0212,W0718


"main"


import getpass
import os
import pathlib
import pwd
import readline
import sys
import termios
import time


from .cli      import CLI
from .commands import Commands, command
from .console  import Console
from .errors   import Errors, errors, later
from .event    import Event
from .help     import TXT
from .log      import Logging
from .parse    import parse
from .persist  import Persist, skel
from .run      import Cfg
from .utils    import spl


from .. import mod as modules
from .. import usr as mods


def cmnd(txt, outer):
    "do a command using the provided output function."
    cli = CLI()
    cli.out = outer
    evn = Event()
    evn.txt = txt
    command(cli, evn)
    evn.wait()
    return evn


def daemon(pidfile, verbose=False):
    "switch to background."
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    if os.path.exists(pidfile):
        os.unlink(pidfile)
    path = pathlib.Path(pidfile)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def init(pkg, modstr, disable=None):
    "scan modules for commands and classes"
    mds = []
    for mod in spl(modstr):
        if disable and mod in spl(disable):
            continue
        module = getattr(pkg, mod, None)
        if not module:
            continue
        if "init" not in dir(module):
            continue
        try:
            module.init()
        except Exception as ex:
            later(ex)
    return mds


def scan(pkg, modstr, disable=None):
    "scan modules for commands and classes"
    mds = []
    dirr = sorted([x for x in dir(pkg) if not x.startswith("__")])
    for modname in spl(modstr):
        if modname not in dirr:
            continue
        if disable and modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        Commands.scan(module)
        Persist.scan(module)
    return mds


def modnames():
    "list all modules."
    return sorted([x for x in dir(modules) + dir(mods) if not x.startswith("__")])


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def wrap(func):
    "reset terminal."
    old3 = None
    try:
        old3 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old3:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old3)


def wrapped():
    "wrap main."
    wrap(main)
    errors()


def main():
    "main"
    Errors.out = print
    readline.redisplay()
    skel()
    parse(Cfg, " ".join(sys.argv[1:]))
    Cfg.dis = Cfg.sets.dis
    Cfg.mod += "," + ",".join(modnames())
    if "h" in Cfg.opts:
        print(TXT)
        return
    if "v" in Cfg.opts:
        Logging.out = Errors.out = print
        dte = " ".join(time.ctime(time.time()).replace("  ", " ").split()[1:])
        print(f'{dte} {Cfg.name.upper()} {Cfg.opts.upper()} {Cfg.mod.upper()}'.replace("  ", " "))
    wait = False
    if "d" in Cfg.opts:
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "-v" in sys.argv)
        privileges(Cfg.user)
        modstr = "," + ",".join(modnames())
        init(modules, modstr)
        init(mods, modstr)
        wait = True
    elif "c" in Cfg.opts:
        csl = Console()
        if "i" in Cfg.opts:
            init(modules, Cfg.mod, Cfg.dis)
            init(mods, Cfg.mod, Cfg.dis)
        csl.start()
        wait = True
    scan(modules, Cfg.mod, Cfg.dis)
    scan(mods, Cfg.mod, Cfg.dis)
    if Cfg.otxt:
        cmnd(Cfg.otxt, print)
    if wait or "w" in Cfg.opts:
        while 1:
            time.sleep(1.0)


def __dir__():
    return (
        'cmnd',
        'daemon',
        'inited',
        'main',
        'modnames',
        'privileges',
        'scanned',
        'wrapped'
    )
