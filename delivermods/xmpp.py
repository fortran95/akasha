import threading
import time

import sleekxmpp

class XMPP(threading.Thread):
    # XMPP queue stores incoming and outgoing messages.
    # Item(s) in the queue are dict(s). Possible keys are: jid, message
    outgoing_queue = None
    incoming_queue = None
    queue_lock = None
    
    connect_status = 0   # 0-disconnected 1-connecting 2-confirm_connected,
                         # -1:error
    schedule_rec   = {'send_presence':0}
    schedule_set   = {'send_presence':30}

    def __init__(self,jid,password):
        threading.Thread.__init__(self)
        self._sig_terminate = threading.Event()

        self.xmpp = sleekxmpp.ClientXMPP(jid,password)

        self.xmpp.add_event_handler("session_start",self._onConnected)
        self.xmpp.add_event_handler("message",self._onMessage)
        self.xmpp.add_event_handler("disconnected",self._onDisconnected)

    def run(self):
        if None in (self.outgoing_queue,self.incoming_queue,self.queue_lock):
            raise Exception("XMPP deliver module not fully initialized.")

        while not self._sig_terminate.isSet():
            nowtime = time.time()

            if   self.connect_status == 0:
                try:
                    self.xmpp.connect()
                    self.xmpp.process(block=False)
                    self.connect_status = 1
                except Exception,e:
                    print "XMPP deliver module: failed connecting: %s" % e
                    self.terminate()
            elif self.connect_status == 2:
                # Scheduled to send presence
                if (nowtime - self.schedule_rec['send_presence'] > 
                        self.schedule_set['send_presence']):
                    self.xmpp.sendPresence()
                    self.schedule_rec['send_presence'] = nowtime

                # empty send queue
                while self.outgoing_queue:
                    message = self.outgoing_queue.pop(0)
                    self.xmpp.sendMessage(mto=message["jid"],
                                          mbody=message["message"],
                                          mtype="chat")
            time.sleep(1)

        # Exiting
        if self.connect_status == 2:
            self.xmpp.disconnect(wait=True)
        return

    def _onConnected(self,event):
#        print "On Connected"
        self.xmpp.sendPresence()
        self.connect_status = 2

    def _onDisconnected(self,event):
#        print "On Disconnected"
        if self.connect_status == 1:
            self.terminate()
        self.connect_status = 0

    def _onMessage(self,message):
#        print "On Message"
        self.queue_lock.acquire()
       
        if message["type"] in ("chat", "normal"):
            self.incoming_queue.append({"jid":message["from"],
                                        "message":message["body"]})

        self.queue_lock.release()

    def terminate(self):
        self._sig_terminate.set()

if __name__ == '__main__':
    q1,q2 = [],[]
    lock = threading.Lock()
    pwd = raw_input('password:')
    x = XMPP('neoatlantis@pidgin.su',pwd)
    x.outgoing_queue,x.incoming_queue = q1,q2
    x.queue_lock = lock
    x.start()
    
    while True:       
        print q2
        cmd = raw_input('COMMAND: t, new')
        if cmd == 't':
            x.terminate()
            x.join()
            del x
            exit()
        if cmd == 'new':
            receiver = 'neoatlantis@wtfismyip.com/'
            message  = raw_input('message?')
            q1.append({"jid":receiver,"message":message})
