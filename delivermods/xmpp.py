import sleekxmpp

class XMPP(object):
    def __init__(self,jid,password):
        self.xmpp = sleekxmpp.ClientXMPP(jid,password)

        self.xmpp.add_event_handler("session_start",self._onConnected)
        self.xmpp.add_event_handler("message",self._onMessage)
        self.xmpp.add_event_handler("disconnected",self._onDisconnected)

    def run(self):
        self.xmpp.connect()
        self.xmpp.process(block=False)

    def _onConnected(self,event):
        self.xmpp.sendPresence()

    def _onDisconnected(self,event):
        pass

    def _onMessage(self,message):
        pass
