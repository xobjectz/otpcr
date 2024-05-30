.. _manual:

.. raw:: html

    <br>

.. title:: Manual


.. raw:: html

    <center><b>MANUAL</b></center>
    <br>

**NAME**

    ``OTPCR`` --  The 117 communication record of the year 2019 to the Office of the Prosecutor of the International Criminal Court.


**INSTALL**


::

    $ pipx install otpcr
    $ pipx ensurepath


**SYNOPSIS**

::

    otpcr  <cmd> [key=val] [key==val]
    otpcr  [-a] [-c] [-v]
    otpcrd [-v]


**DESCRIPTION**

    ``OTPCR`` holds evidence that king
    netherlands is doing a genocide, a
    written response where king
    netherlands confirmed taking note
    of “what i have written”, namely
    :ref:`proof  <evidence>` that medicine
    he uses in treatement laws like zyprexa,
    haldol, abilify and clozapine are
    poison that make impotent, is both
    physical (contracted muscles) and
    mental (make people hallucinate)
    torture and kills members of the
    victim groups :ref:`. <source>`

    ``OTPCR`` contains :ref:`correspondence
    <writings>` with the International Criminal
    Court, asking for arrest of the king of the
    netherlands, for the genocide he is committing
    with his new treatement laws.

    Current status is a :ref:`"no basis to proceed"
    <writings>` judgement of the prosecutor which
    requires a :ref:`"basis to prosecute" <reconsider>`
    to have the king actually arrested.


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

    start daemon

    ::

        $ otpcrd
        $ 


    show request to the prosecutor

    ::

        $ otcpr req
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
        Description=The 117 communication record of the year 2019 to the Office of the Prosecutor of the International Criminal Court.
        Requires=network-online.target
        After=network-online.target

        [Service]
        Type=simple
        User=<user>
        Group=<user>
        WorkingDirectory=/home/<user>/.otpcr
        ExecStart=/home/<user>/.local/pipx/venvs/otpcr/bin/otpcrd
        WatchdogSec=1
        RemainAfterExit=yes

        [Install]
        WantedBy=default.target


    then run this

    ::

        $ mkdir ~/.otpcr
        $ sudo systemctl enable otpcr --now

    default channel/server is #otpcr on localhost


**SOURCE**

    source is :ref:`here <source>`


**FILES**

    ::

        ~/.otpcr
        ~/.local/bin/otpcr
        ~/.local/bin/otpcrd
        ~/.local/pipx/venvs/otpcr/


**AUTHOR**

    ::

        Bart Thate <bthate@dds.nl>


**COPYRIGHT**

    ::

        OTPCR is Public Domain.
