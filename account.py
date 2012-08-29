import hashlib

class Account(object):
    user_id = ''
    transmitter = None
    def getStatus():
        pass
    def getID():
        pass
    def send(): # TODO renew signature
        pass
    def fetch(): # TODO renew signature
        pass # TODO fetch message queue

class JabberAccount(Account):
    def getID():
        return hashlib.md5(self.user_id).hexdigest().lower()

def byID_Protocol(userid,protocol):
    # Returns an Account class by searching 
    pass
