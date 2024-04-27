# This file is placed in the Public Domain.


"main"


import getpass
import os
import pwd
import readline
import sys
import termios
import time


from .client  import Client, cmnd, parse_cmd, spl
from .default import Default
from .errors  import debug, enable, errors, later
from .event   import Event
from .object  import cdir
from .runtime import broker
from .workdir import Workdir, skel


from .command   import scan as scancmd
from .whitelist import scan as scancls


from . import modules


Cfg             = Default()
Cfg.dis         = ""
Cfg.mod         = ""
Cfg.opts        = ""
Cfg.name        = __file__.split(os.sep)[-2]
Cfg.version     = "8"
Cfg.wdr         = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile     = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Workdir.workdir = Cfg.wdr


dte = time.ctime(time.time()).replace("  ", " ")


class Console(Client):

    "Console"

    def __init__(self):
        Client.__init__(self)
        broker.add(self)

    def announce(self, txt):
        "disable announce."

    def callback(self, evt):
        "wait for callback."
        Client.callback(self, evt)
        evt.wait()

    def poll(self):
        "poll console and create event."
        evt = Event()
        evt.orig = object.__repr__(self)
        evt.txt = input("> ")
        evt.type = "command"
        return evt

    def say(self, _channel, txt):
        "print to console"
        txt = txt.encode('utf-8', 'replace').decode()
        print(txt)


def daemon(pidfile, verbose=False):
    "switch to background."
    # pylint: disable=W0212
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
    cdir(os.path.dirname(pidfile))
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


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
            try:
                module.init()
                mds.append(module)
            except Exception as ex: # pylint: disable=W0718
                later(ex)
    return mds


def scan(pkg, modstr, disable=""):
    "scan modules for commands and classes"
    mds = []
    for modname in spl(modstr):
        if skip(modname, disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        scancmd(module)
        scancls(module)
    return mds


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def skip(name, skipped):
    "check for skipping"
    for skp in spl(skipped):
        if skp in name:
            return True
    return False


def wrap(func):
    "restore console."
    old2 = None
    try:
        old2 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old2:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old2)


def ver(event):
    "show version."
    event.reply(f"{Cfg.name.upper()} {Cfg.version}")


def main():
    "main"
    enable(print)
    skel()
    parse_cmd(Cfg, " ".join(sys.argv[1:]))
    if Cfg.sets.dis:
        Cfg.dis += "," + Cfg.sets.dis
    Cfg.mod = ",".join(modules.__dir__())
    if "v" in Cfg.opts:
        debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    scan(modules, Cfg.mod, Cfg.dis)
    if "h" in Cfg.opts:
        print(__doc__)
    elif "d" in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "v" in Cfg.opts)
        privileges(Cfg.user)
        init(modules, Cfg.mod, Cfg.dis)
        while 1:
            time.sleep(1.0)
    elif "c" in Cfg.opts:
        init(modules, Cfg.mod, Cfg.dis)
        csl = Console()
        csl.start()
        while 1:
            time.sleep(1.0)
    elif Cfg.otxt:
        cmnd(Cfg.otxt, print)


def wrapped():
    "wrap main function."
    wrap(main)


if __name__ == "__main__":
    readline.redisplay()
    wrapped()
    errors()
