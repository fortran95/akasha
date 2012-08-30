import os,sys

def localpath(*p):
    return os.path.join(os.path.realpath(os.path.dirname(sys.argv[0])),*p)
