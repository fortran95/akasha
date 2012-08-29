# -*- coding: utf-8 -*-

# Session Manager, can be fired either from a call within other codes, or from a command-line command.
# The first occasion will return a callback that enables codes to add new messages.

import argparse,sys,os
from translate import t

def message_arrival(user,buddy,message):
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=t('Session manager for individual users.'))
    parser.add_argument('--user' ,'-u',action='store',dest='user' ,help=t("Specify the user that talks with others."))
    parser.add_argument('--buddy','-b',action='store',dest='buddy',help=t("Specify the one that the user talks with."))

    args = parser.parse_args(sys.argv[1:])

    if args.user == None or args.buddy == None:
        parser.print_help()
        exit()

    # now we are going to display a session window that displays chat logs and accepts new messages.
