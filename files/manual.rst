.. _manual:

.. raw:: html

    <br>

.. title:: Manual


.. raw:: html

    <center><b>MANUAL</b></center>
    <br>

**NAME**

    ``GENOCIDE``  --  Reconsider OTP-CR-117/19.


**INSTALL**


::

    $ pipx install genocide
    $ pipx ensurepath


**SYNOPSIS**

::

    genocide  <cmd> [key=val] [key==val]
    genocide  [-a] [-c] [-v]
    genocided [-v]


**DESCRIPTION**

    ``GENOCIDE`` holds evidence that king
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

    ``GENOCIDE`` contains :ref:`correspondence
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

        $ genocide
        $

    see list of commands

    ::

        $ genocide cmd
        cmd,dne,err,log,mod,req,tdo,thr,tmr


    start a console

    ::

        $ genocide -c 
        >

    use -v for verbose

    ::

        $ genocide -cv
        May 12 05:51:49 2024 GENOCIDE CV CMD,ERR,LOG,MOD,REQ,TDO,THR,TMR
        >

    start daemon

    ::

        $ genocided
        $ 


    show request to the prosecutor

    ::

        $ genocide req
        Information and Evidence Unit
        Office of the Prosecutor
        Post Office Box 19519
        2500 CM The Hague
        The Netherlands


**CONFIGURATION**

    irc

    ::

        $ genocide cfg server=<server>
        $ genocide cfg channel=<channel>
        $ genocide cfg nick=<nick>

    sasl

    ::

        $ genocide pwd <nsvnick> <nspass>
        $ genocide cfg password=<frompwd>

    rss

    ::

        $ genocide rss <url>
        $ genocide dpl <url> <item1,item2>
        $ genocide rem <url>
        $ genocide nme <url> <name>


**COMMANDS**

    ::

        cfg - irc configuration
        cmd - commands
        mre - displays cached output
        now - show genocide stats
        pwd - sasl nickserv name/pass
        req - reconsider
        wsd - show wisdom


**SYSTEMD**

    save the following it in /etc/systemd/system/genocide.service
    and replace "<user>" with the user running pipx

    ::
 
        [Unit]
        Description=Reconsider OTP-CR-117/19.
        Requires=network-online.target
        After=network-online.target

        [Service]
        Type=simple
        User=<user>
        Group=<user>
        WorkingDirectory=/home/<user>/.genocide
        ExecStart=/home/<user>/.local/pipx/venvs/genocide/bin/genocided
        RemainAfterExit=yes

        [Install]
        WantedBy=default.target


    then run this

    ::

        $ mkdir ~/.genocide
        $ sudo systemctl enable genocide --now

    default channel/server is #genocide on localhost


**SOURCE**

    source is :ref:`here <source>`


**FILES**

    ::

        ~/.genocide
        ~/.local/bin/genocide
        ~/.local/bin/genocided
        ~/.local/pipx/venvs/genocide/


**AUTHOR**

    ::

        Bart Thate <bthate@dds.nl>


**COPYRIGHT**

    ::

        GENOCIDE is Public Domain.
