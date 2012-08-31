# -*- coding: utf-8 -*-
import urwid

class Screen(object):
    
    def __init__(self):
        palette = [('banner', 'black', 'light gray', 'standout,underline'),
                   ('streak', 'black', 'dark red', 'standout'),
                   ('bg', 'black', 'dark blue'),]

        self._createWidgets()

        urwid.MainLoop(self.main,palette).run()
    
    def _getAccountScreens(self):
        self._accountScreen = [
            urwid.Text('Account1'),
            urwid.Text('Account2'),
        ]
        return self._accountScreen
    def _getEntities(self):
        self._entities = []
        return self._entities()

    def _createWidgets(self):
        self.statusListWalker = urwid.SimpleListWalker(self._getAccountScreens())
        self.statusList = urwid.AttrMap(urwid.ListBox(self.statusListWalker),'bg')

        self.left  = urwid.BoxAdapter(self.statusList,40)
        self.right = urwid.LineBox(urwid.Text("Help:\n F1-Exit F2-Enter"))
        
        self.cols = urwid.Columns([self.left,
                             ('fixed',20,self.right)]
                            ,1)

        self.main = urwid.Filler(self.cols)

s = Screen()
