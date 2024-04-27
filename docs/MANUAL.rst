NAME

::

    OTPCR - The 117 communication record of the year 2019 to the Office
            of the Prosecutor of the International Criminal Court.


SYNOPSIS

::

    otpcr <cmd> [key=val] [key==val]
    otpcr [-a] [-c] [-d] [-h] [-v]

    options are:

    -a     load all modules
    -c     start console
    -d     start daemon
    -h     display help
    -v     use verbose


DESCRIPTION

::

    OTPCR contains all the python3 code to program objects in a functional
    way. It provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    OTPCR allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    OTPCR has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    OTPCR has a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    OTPCR is Public Domain.


INSTALL

::

    use pipx to install otpcr as a local installed program

    $ pipx install otpcr
    $ pipx ensurepath
    $ mkdir ~/.otpcr


CONFIGURATION

::

    $ otpcr cfg 
    channel=#otpcr commands=True nick=otpcr port=6667 server=localhost

    irc

    $ otpcr cfg server=<server>
    $ otpcr cfg channel=<channel>
    $ otpcr cfg nick=<nick>

    sasl

    $ otpcr pwd <nsvnick> <nspass>
    $ otpcr cfg password=<frompwd>

    rss

    $ otpcr rss <url>
    $ otpcr dpl <url> <item1,item2>
    $ otpcr rem <url>
    $ otpcr nme <url> <name>


USAGE

::

    without any argument the program does nothing

    $ otpcr
    $

    see list of commands

    $ otpcr cmd
    cfg,cmd,dne,dpl,exp,log,mre,nme,pwd,rem,req,res,rss,tdo,ver

    list of modules

    $ otpcr mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ otpcr -c

    use mod=<name1,name2> to load additional modules

    $ otpcr -c mod=irc,rss
    >

    use -v for verbose

    $ otpcr -cv mod=irc
    OTPCR started CV started Sat Dec 2 17:53:24 2023
    >


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    thr - show the running threads


SYSTEMD


save the following it in /etc/systemd/system/otpcr.service and
replace "<user>" with the user running pipx

::

    [Unit]
    Description=OTP-CR-117/19
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.otpcr
    ExecStart=/home/<user>/.local/pipx/venvs/otpcr/bin/otpcr -d
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

then run this

::

    $ sudo systemctl enable otpcr --now


default channel/server is #otpcr on localhost

FILES

::

    ~/.otpcr
    ~/.local/bin/otpcr
    ~/.local/pipx/venvs/otpcr/

AUTHOR

::

    Bart Thate <bthate@dds.nl>

COPYRIGHT

::

    OTPCR is Public Domain.
