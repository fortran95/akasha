# -*- coding: utf-8 -*-
import urwid

class Screen(object):
    
    def __init__(self):
        palette = [('normal', 'white', 'dark blue'),
                   ('banner', 'black', 'light gray', 'standout,underline'),
                   ('streak', 'black', 'dark red', 'standout'),
                   ('bg', 'black', 'dark blue'),]

        self._createWidgets()

        urwid.MainLoop(self.main,palette).run()
    
    def _getAccountScreens(self):
        self._accountLights = {}
        self._accountScreen = []
        for account in ('neoatlantis@pidgin.su','sample@jabber.org','someone@somesite.net'):
            self._accountLights[account] = []
            buddies = range(0,30)
            
            for buddy in buddies:
                light = urwid.AttrMap(urwid.Text(str(buddy)),'streak')
                self._accountLights[account].append(light)

            pad = urwid.LineBox(urwid.GridFlow(self._accountLights[account],
                                               10,1,1,'left'),
                                title=account)
            padlight = urwid.AttrMap(pad,'banner')
            self._accountScreen.append(padlight)

        return self._accountScreen
    def _getEntities(self):
        self._entities = []
        return self._entities()

    def _createWidgets(self):
        self.statusListWalker = urwid.SimpleListWalker(self._getAccountScreens())
        self.statusList = urwid.ListBox(self.statusListWalker)

        self.left  = urwid.BoxAdapter(self.statusList,32)
        self.right = urwid.AttrMap(
                                   urwid.LineBox(
                                        urwid.Text("Help:\n F1-Exit F2-Enter")),
                                   'normal')
        
        self.cols = urwid.Columns([self.left,
                                   ('fixed',32,self.right)]
                                 ,1)

        self.main = urwid.Filler(self.cols)

s = Screen()
