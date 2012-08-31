# -*- coding: utf-8 -*-
import urwid

class Screen(object):
    
    def __init__(self):
        palette = [('lights.available', 'white', 'dark green'),
                   ('lights.connecting', 'white', 'brown'),
                   ('lights.unavailable', 'white', 'dark red'),
                   ('pads.available', 'white', 'dark blue'),
                   ('pads.unavailable', 'black', 'light gray'),
                   ('default', 'white', 'dark blue'),
                  ]

        self._createWidgets()
        def handler(input):
            if input in 'abcABC':
                self._accountScreen[ord(input)-ord('a')].set_attr_map({None:'pads.available'})
            if input in '0123456789':
                self._accountLights['neoatlantis@pidgin.su'][ord(input) - ord('0')].set_attr_map({None:'lights.connecting'})
            if input in ('q','Q'):
                raise urwid.ExitMainLoop()
        urwid.MainLoop(self.main,palette,unhandled_input=handler).run()
    
    def _getAccountScreens(self):
        self._accountLights = {}
        self._accountScreen = []
        for account in ('neoatlantis@pidgin.su','sample@jabber.org','someone@somesite.net'):
            self._accountLights[account] = []
            buddies = range(0,30)
            
            for buddy in buddies:
                light = urwid.AttrMap(urwid.Text(str(buddy)),'lights.unavailable')
                self._accountLights[account].append(light)

            pad = urwid.LineBox(urwid.GridFlow(self._accountLights[account],
                                               10,1,1,'left'),
                                title=account)
            padlight = urwid.AttrMap(pad,'pads.unavailable')
            self._accountScreen.append(padlight)

        return self._accountScreen
    def _getEntities(self):
        self._entities = []
        return self._entities()

    def _createWidgets(self):
        self.statusListWalker = urwid.SimpleListWalker(self._getAccountScreens())
        self.statusList = urwid.ListBox(self.statusListWalker)

        self.left  = urwid.BoxAdapter(self.statusList,60)
        self.right = urwid.AttrMap(
                                   urwid.LineBox(
                                        urwid.Text("Help:\n F1-Exit F2-Enter")),
                                   'default')
        
        self.cols = urwid.Columns([self.left,
                                   ('fixed',32,self.right)]
                                 ,1)

        self.main = urwid.Filler(self.cols)

s = Screen()
