# This file is placed in the Public Domain.
#
#


"help"


SEP = "/"
NAME = __file__.split(SEP)[-3]
TXT = f"""{NAME.upper()}

    {NAME}  <cmd> [key=val] [key==val]
    {NAME}  [-a] [-c] [-d] [-h] [-v]

OPTIONS

    -a     load all modules
    -c     start console
    -d     run in the background
    -h     show help
    -i     start services
    -v     use verbose

COMMANDS
    
    $ {NAME} cmd
    cfg,cmd,dpl,err,exp,imp,mod,mre,nme,pwd,rem,res,rss,thr

INIT

    $ {NAME} -cvi mod=irc,rss
"""
