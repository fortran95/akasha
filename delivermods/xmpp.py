import threading
import time

import sleekxmpp

class XMPP(threading.Thread):
    # XMPP queue stores incoming and outgoing messages.
    # Item(s) in the queue are dict(s). Possible keys are: jid, message
    outgoing_queue = None
    incoming_queue = None
    queue_lock = None
    
    connect_status = 0   # 0-disconnected 1-connecting 2-confirm_connected
    schedule_rec   = {'send_presence':0}
    schedule_set   = {'send_presence':30}

    def __init__(self,jid,password):
        threading.Thread.__init__(self)

        self.xmpp = sleekxmpp.ClientXMPP(jid,password)

        self.xmpp.add_event_handler("session_start",self._onConnected)
        self.xmpp.add_event_handler("message",self._onMessage)
        self.xmpp.add_event_handler("disconnected",self._onDisconnected)

    def run(self):
        if None in (self.outgoing_queue,self.incoming_queue,self.queue_lock):
            raise Exception("XMPP deliver module not fully initialized.")

        nowtime = time.time()

        if   self.connect_status == 0:
            self.xmpp.connect()
            self.xmpp.process(block=False)
            self.connect_status = 1
        elif self.connect_status == 2:
            # Scheduled to send presence
            if (nowtime - self.schedule_rec['send_presence'] > 
                    self.schedule_set['send_presence']):
                self.xmpp.sendPresence()
                self.schedule_rec['send_presence'] = nowtime

            # empty send queue
            while self.outgoing_queue:
                message = self.outgoing_queue.pop(0)
                self.xmpp.sendMessage(message["jid"],message["message"])
            

    def _onConnected(self,event):
        self.xmpp.sendPresence()
        self.connect_status = 2

    def _onDisconnected(self,event):
        self.connect_status = 0

    def _onMessage(self,message):
        self.queue_lock.acquire()

        self.incoming_queue.append(message)
        print message

        self.queue_lock.release()

if __name__ == '__main__':
    q1,q2 = [],[]
    lock = threading.Lock()
    pwd = raw_input('password:')
    x = XMPP('neoatlantis@pidgin.su',pwd)
    x.outgoing_queue,x.incoming_queue = q1,q2
    x.queue_lock = lock
    x.start()
    x.join()
