**NAME**

::

    OTPCR - The 117 communication record of the year 2019 to the Office of the Prosecutor
            of the International Criminal Court.


**INSTALL**


::

    $ pipx install otpcr
    $ pipx ensurepath
    $ mkdir ~/.otpcr


**SYNOPSIS**

::

    otpcr  <cmd> [key=val] [key==val]
    otpcr  [-a] [-c] [-d] [-i] [-v]

    options are:

    -a     load all modules
    -c     start console
    -d     run in the background
    -h     show help
    -i     start services
    -v     use verbose


**DESCRIPTION**

::

    OTPCR holds evidence that king netherlands
    is doing a genocide, a written response where
    king netherlands confirmed taking note of “what
    i have written”, namely proof that medicine he
    uses in treatement laws like zyprexa, haldol,
    abilify and clozapine are poison that make impotent,
    is both physical (contracted muscles) and mental
    (make people hallucinate) torture and kills members
    of the victim groups.

    OTPCR contains correspondence with the International
    Criminal Court, asking for the arrest of king
    netherlands, for the genocide he is committing with
    his new treatement laws.

    Current status is a "no basis to proceed" judgement of
    the prosecutor which requires a "basis to prosecute" to
    have the king actually arrested and, thereby, his genocide
    stopped.


**USAGE**

without any argument the bot does nothing

::

    $ otpcr
    $

see list of commands

::

    $ otpcr cmd
    cmd,dne,err,log,mod,req,tdo,thr,tmr


start a console

::

    $ otpcr -c 
    >

use -v for verbose

::

    $ otpcr -cv
    May 12 05:51:49 2024 OTPCR CV CMD,ERR,LOG,MOD,REQ,TDO,THR,TMR
    >

use -i to run init on modules

::

    $ otpcr -caiv 

start daemon

::

    $ otpcr -d


show request to the prosecutor

::

    $ otpcr req
    Information and Evidence Unit
    Office of the Prosecutor
    Post Office Box 19519
    2500 CM The Hague
    The Netherlands


**CONFIGURATION**

irc

::

    $ otpcr cfg server=<server>
    $ otpcr cfg channel=<channel>
    $ otpcr cfg nick=<nick>

sasl

::

    $ otpcr pwd <nsvnick> <nspass>
    $ otpcr cfg password=<frompwd>

rss

::

    $ otpcr rss <url>
    $ otpcr dpl <url> <item1,item2>
    $ otpcr rem <url>
    $ otpcr nme <url> <name>


opml

::

    $ otpcr imp <filename>
    $ otpcr exp


**COMMANDS**

::

    cfg - irc configuration
    cmd - commands
    mre - displays cached output
    pwd - sasl nickserv name/pass
    req - reconsider


**SYSTEMD**

save the following it in /etc/systemd/system/otpcr.service
and replace "<user>" with the user running pipx

::
 
    [Unit]
    Description=The 117 communication record of the year 2019 to the Office of the Prosecutor of the International Criminal Court
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


**FILES**

::

    ~/.otpcr
    ~/.local/bin/otpcr
    ~/.local/pipx/venvs/otpcr/*


**AUTHOR**

::

    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

::

    OTPCR is Public Domain.
