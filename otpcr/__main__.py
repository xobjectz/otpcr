# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212,E0402,W0105


"objects client"


import getpass
import os
import pwd
import readline
import sys
import termios
import time


import otpcr


from .default import Default
from .handler import Client, Event, cmnd
from .runtime import Errors, debug, forever, init, parse_cmd
from .persist import Workdir


Cfg         = Default()
Cfg.mod     = "cmd,mod"
Cfg.name    = "otpcr"
Cfg.version = 1
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
Workdir.wd = Cfg.wd


class Console(Client):

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
    Workdir.cdir(os.path.dirname(pidfile))
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def privileges(username):
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


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


"runtime"


def cmd(event):
    event.reply(",".join(sorted(list(Client.cmds))))


def ver(event):
    event.reply(f"OBJX {Cfg.version}")
    

def main():
    Client.add(cmd)
    Client.add(ver)
    Workdir.skel()
    Errors.enable(print)
    parse_cmd(Cfg, " ".join(sys.argv[1:]))
    readline.redisplay()
    if 'a' in Cfg.opts:
        Cfg.mod = ",".join(otpcr.__dir__())
    if "v" in Cfg.opts:
        dte = time.ctime(time.time()).replace("  ", " ")
        debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    if "h" in Cfg.opts:
        from . import __doc__ as txt
        print(txt)
        return
    if "d" in Cfg.opts:
        Cfg.mod = ",".join(otpcr.__dir__())
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "v" in Cfg.opts)
        privileges(Cfg.user)
        Cfg.mod = ",".join([x for x in otpcr.__dir__() if len(x) == 3])
        init(otpcr, Cfg.mod)
        forever()
        return
    if "c" in Cfg.opts:
        init(otpcr, Cfg.mod)
        csl = Console()
        if 'z' in Cfg.opts:
            csl.threaded = False
        csl.start()
        forever()
        return
    if Cfg.otxt:
        Cfg.mod = ",".join([x for x in otpcr.__dir__() if len(x) == 3])
        return cmnd(Cfg.otxt, print)


def wrapped():
    wrap(main)
    Errors.show()


if __name__ == "__main__":
    wrapped()
