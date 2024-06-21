# This file is placed in the Public Domain.
#
# pylint: disable=W0125


"command line interface"


from ..lib.iface   import Object

from .commands import command
from .handler  import Handler


class CLI(Handler):

    "CLI"

    cache = Object()
    out = print

    def __init__(self):
        Handler.__init__(self)
        self.register("command", command)

    def say(self, _channel, txt):
        "echo on verbose."
        self.raw(txt)

    def raw(self, txt):
        "print to screen."
        if self.out:
            txt = txt.encode('utf-8', 'replace').decode()
            self.out(txt)

    def show(self, evt):
        "show results into a channel."
        for txt in evt.result:
            self.say(evt.channel, txt)


def __dir__():
    return (
       'CLI',
    )
