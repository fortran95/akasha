# -*- coding: utf-8 -*-

import argparse,sys,os
from translate import t

parser = argparse.ArgumentParser(description=t('Session manager for individual users.'))
parser.add_argument('--user' ,'-u',action='store',dest='user' ,help=t("Specify the user that talks with others."))
parser.add_argument('--buddy','-b',action='store',dest='buddy',help=t("Specify the one that the user talks with."))

args = parser.parse_args(sys.argv[1:])
