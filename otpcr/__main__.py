# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0105,W0201,W0212,W0613,E0401,E0402,W0611
# ruff: noqa: E402


"""NAME

    OTPCR - 117/19

SYNOPSIS

    otpcr <cmd> [key=val] [key==val]

OPTIONS

    -a     load all modules
    -c     start console
    -d     start daemon
    -h     display help
    -v     use verbose

EXAMPLE

    otpcr -cav

COPYRIGHT

    OTPCR is Public Domain."""


"main"


import getpass
import os
import pwd
import readline
import sys
import termios
import time


sys.path.insert(0, os.getcwd())


from otpcr.client  import Client, cmnd, parse_cmd, spl
from otpcr.command import Command
from otpcr.default import Default
from otpcr.errors  import debug, enable, errors
from otpcr.event   import Event
from otpcr.object  import cdir
from otpcr.runtime import broker
from otpcr.workdir import Workdir, skel


from otpcr import modules


if os.path.exists("mods"):
    import mods
else:
    mods = None


Cfg             = Default()
Cfg.mod         = "cmd,mod"
Cfg.opts        = ""
Cfg.name        = "otpcr"
Cfg.version     = "5"
Cfg.wd          = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile     = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Workdir.workdir = Cfg.wd


dte = time.ctime(time.time()).replace("  ", " ")


class Console(Client):

    def __init__(self):
        Client.__init__(self)
        broker.add(self)

    def announce(self, txt):
        pass

    def callback(self, evt):
        Client.callback(self, evt)
        evt.wait()

    def poll(self):
        evt = Event()
        evt.orig = object.__repr__(self)
        evt.txt = input("> ")
        evt.type = "command"
        return evt

    def say(self, channel, txt):
        txt = txt.encode('utf-8', 'replace').decode()
        print(txt)


def daemon(pidfile, verbose=False):
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


def privileges(username):
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def skip(name, skipped):
    for skp in spl(skipped):
        if skp in name:
            return True
    return False


def wrap(func):
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
    event.reply(f"{Cfg.name.upper()} {Cfg.version}")


def main():
    Command.add(ver)
    enable(print)
    skel()
    parse_cmd(Cfg, " ".join(sys.argv[1:]))
    if 'a' in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
        if mods:
            Cfg.mod += "," + ",".join(mods.__dir__())
    if "v" in Cfg.opts:
        debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    if "h" in Cfg.opts:
        print(__doc__)
        return
    if "d" in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "v" in Cfg.opts)
        privileges(Cfg.user)
        init(modules, Cfg.mod)
        while 1:
            time.sleep(1.0)
        return
    if "c" in Cfg.opts:
        init(modules, Cfg.mod, Cfg.sets.dis)
        if mods:
            Cfg.mod += "," + ",".join(mods.__dir__())
            init(mods, Cfg.mod)
        csl = Console()
        csl.start()
        while 1:
            time.sleep(1.0)
        return
    if Cfg.otxt:
        return cmnd(Cfg.otxt, print)


def daemoned():
    Cfg.opts += "d"
    main()


def wrapped():
    wrap(main)
    errors()


if __name__ == "__main__":
    wrapped()
