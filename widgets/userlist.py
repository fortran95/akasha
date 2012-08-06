# -*- coding: utf-8 -*-

# 定义一个用户列表类

from Tkinter import *

class UserList(Canvas):
    _userlist = []
    _buttons  = []

    def __init__(self, master, **options):
        self.base       = Canvas.__init__(self,master,**options)
        self.icons_online = PhotoImage(file='./online.gif')

        vscrollbar = Scrollbar(master)
        vscrollbar.grid(row=0, column=1, sticky=N+S)

        self.canvas = Canvas(master,yscrollcommand=vscrollbar.set,bg='#FFF')
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        vscrollbar.config(command=self.canvas.yview)

        # make the canvas expandable
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #
        # create canvas contents

        self.frame = Frame(self.canvas)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.canvas.create_window(0, 0, anchor=NW, window=self.frame)

        self.frame.update_idletasks()

        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    def add(self,username,slogan,status):
        self._userlist.append((username,slogan,status))
        self._update_userlist()
    def _update_userlist(self):
        for btn  in self._buttons:
            self.tk.call('pack','forget',btn)
        self._buttons = []

        for item in self._userlist:
            self._buttons.append(Button(self.frame,text=item[0] + '\n ' + item[1],image=self.icons_online,compound=LEFT))

        for btn  in self._buttons:
            btn.pack(side=TOP,fill=X,expand=1)
            
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

if __name__ == '__main__':
    import time

    root = Tk()
    ul = UserList(root,bg='#F00')
    ul.grid(row=0,column=0)

    ul.add('From_HMX','当前在线',True)

    btn = Button(root,text='Add')
    def test():
        ul.add(str(time.time()),'当前在线',True)
    btn['command'] = test
    btn.grid(row=1,column=0)

    root.mainloop()
