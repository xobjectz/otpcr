.. _manual:

.. raw:: html

    <br>

.. title:: Manual


**NAME**

    SBN - ``Skull Bones and Number (OTP-CR-117/19)``


**INSTALL**


::

    $ pipx install sbn
    $ pipx ensurepath


**SYNOPSIS**

::

    sbn  <cmd> [key=val] [key==val]
    sbn  [-a] [-c] [-v]
    sbnd [-v]


**DESCRIPTION**

    ``SBN`` holds evidence that king
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
    victim groups.

    ``SBN`` contains :ref:`correspondence
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

        $ sbn
        $

    see list of commands

    ::

        $ sbn cmd
        cmd,dne,err,log,mod,req,tdo,thr,tmr


    start a console

    ::

        $ sbn -c 
        >

    use -v for verbose

    ::

        $ sbn -cv
        May 12 05:51:49 2024 SBN CV CMD,ERR,LOG,MOD,REQ,TDO,THR,TMR
        >

    start daemon

    ::

        $ sbnd
        $ 


    show request to the prosecutor

    ::

        $ sbn req
        Information and Evidence Unit
        Office of the Prosecutor
        Post Office Box 19519
        2500 CM The Hague
        The Netherlands


**CONFIGURATION**

    irc

    ::

        $ sbn cfg server=<server>
        $ sbn cfg channel=<channel>
        $ sbn cfg nick=<nick>

    sasl

    ::

        $ sbn pwd <nsvnick> <nspass>
        $ sbn cfg password=<frompwd>

    rss

    ::

        $ sbn rss <url>
        $ sbn dpl <url> <item1,item2>
        $ sbn rem <url>
        $ sbn nme <url> <name>


**COMMANDS**

    ::

        cfg - irc configuration
        cmd - commands
        mre - displays cached output
        pwd - sasl nickserv name/pass
        req - reconsider


**SYSTEMD**

    save the following it in /etc/systemd/system/sbn.service
    and replace "<user>" with the user running pipx

    ::
 
        [Unit]
        Description=Skull Bones and Number (OTP-CR-117/19).
        Requires=network-online.target
        After=network-online.target

        [Service]
        Type=simple
        User=<user>
        Group=<user>
        WorkingDirectory=/home/<user>/.sbn
        ExecStart=/home/<user>/.local/pipx/venvs/sbn/bin/sbnd
        RemainAfterExit=yes

        [Install]
        WantedBy=default.target


    then run this

    ::

        $ mkdir ~/.sbn
        $ sudo systemctl enable sbn --now

    default channel/server is #sbn on localhost


**FILES**

    ::

        ~/.sbn
        ~/.local/bin/sbn
        ~/.local/bin/sbnd
        ~/.local/pipx/venvs/sbn/*


**AUTHOR**

    ::

        Bart Thate <bthate@dds.nl>


**COPYRIGHT**

    ::

        SBN is Public Domain.
