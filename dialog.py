# -*- coding: utf-8 -*-

# 聊天对话框

from Tkinter import *
from widgets import dialogbox

class DialogWindow(object):
    def __init__(self,local,remote):
        self.local,self.remote = local,remote

        self._init_window()
    def _init_window(self):
        self.root = Tk()

        self.remotelabel = Label(text='对方是：[%s]' % self.remote.name,anchor=W,font='sans 9 bold')
        self.dialog = dialogbox.DialogBox(self.root)

        self.remotelabel.grid(row=0,column=0,sticky=N+S+W+E,pady=5,padx=3)
        self.dialog.grid(row=1,column=0)

    def showdialog(self):
        self.root.mainloop()

if __name__ == '__main__':
    from entity import entity

    s = entity('a')
    r = entity('b')

    frm = DialogWindow(s,r)
    frm.showdialog()
