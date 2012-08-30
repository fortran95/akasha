import hashlib,os,time,ConfigParser,shelve
from utils import localpath

class Account(object):
    user_id = ''
    transmitter = None
    def getStatus(self):
        pass
    def getID(self):
        pass
    def send(self): # TODO renew signature
        pass
    def fetch(self): # TODO renew signature
        pass # TODO fetch message queue
    def __init__(self):
        pass

class JabberAccount(Account):
    def getID():
        return hashlib.md5(self.user_id).hexdigest().lower()

def _get_cache():
    need_regenerate = False
    nowtime         = time.time()
    cachepath       = localpath('userdata','entities.cache')

    need_regenerate = not os.path.isfile(cachepath)

    lsresult         = os.listdir(localpath('userdata','entities'))
    credential_paths = {}
    for entityname in lsresult:
        p = localpath('userdata','entities',entityname,'credentials.cfg')
        if not os.path.isfile(p):
            continue
        if need_regenerate == False and os.path.getmtime(p) >= nowtime:
            need_regenerate = True
            os.remove(cachepath)
        credential_paths[entityname] = p

    if need_regenerate: 
        # read all credentials into a cache
        sh = shelve.open(cachepath,writeback=True)
        cfgparser = ConfigParser.ConfigParser()
        for entityname in credential_paths:
            sh[entityname] = {}
            try:
                cfgparser.read(credential_paths[entityname])
                for secname in cfgparser.sections():
                    protocol = cfgparser.get(secname,'protocol').strip().lower()
                    if   protocol == 'xmpp':
                        login = cfgparser.get(secname,'login').strip()
                        sh[entityname][secname] = {'type':'xmpp','login':login}
            except Exception,e:
                print str(e)
        sh.close()

    return shelve.open(cachepath)                   


def byID_Protocol(userid,protocol):
    # Returns an Account class by searching 
    pass

if __name__ == '__main__':
    print _get_cache()
