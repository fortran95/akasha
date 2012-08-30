import threading
import time

import sleekxmpp

class XMPP(threading.Thread):
    outgoing_queue = None
    incoming_queue = None
    
    connected = 0   # 0-disconnected 1-connecting 2-confirm_connected
    schedule  = {'send_presence':0}

    def __init__(self,jid,password):
        self.xmpp = sleekxmpp.ClientXMPP(jid,password)

        self.xmpp.add_event_handler("session_start",self._onConnected)
        self.xmpp.add_event_handler("message",self._onMessage)
        self.xmpp.add_event_handler("disconnected",self._onDisconnected)

    def run(self):
        nowtime = time.time()

        if   self.connected == 0:
            self.xmpp.connect()
            self.xmpp.process(block=False) # TODO questioned
            self.connected = 1
        elif self.connected == 2:
            # Schedule to send presence
            

    def _onConnected(self,event):
        self.xmpp.sendPresence()
        self.connected = 2

    def _onDisconnected(self,event):
        self.connected = 0

    def _onMessage(self,message):
        self.xmpp.sendMessage(message["jid"],message["message"])
