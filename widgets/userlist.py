# -*- coding: utf-8 -*-

# 定义一个用户列表类

from Tkinter import *

class ListItem(Frame):
    def __init__(self, master, **options):
        Frame.__init__(self,master,**options)
        self.master = master

    def itemize(self,username,status,icon,tag=''):
        self.innerframe = Frame(self)

        self.tag = tag

        self.label   = Label(self.innerframe,anchor=W,text=username)
        self.status  = Label(self.innerframe,anchor=W,text=status)

        self.iconimg = PhotoImage(file=icon)
        self.icon    = Label(self.innerframe,image=self.iconimg)
        self.icon.image = self.iconimg

        self.icon.grid  (row=0,column=0,rowspan=2)
        self.label.grid (row=0,column=1,sticky=N+S+W+E)
        self.status.grid(row=1,column=1,sticky=N+S+W+E)

        self.innerframe.grid(row=0,column=0,padx=3,pady=3)

        self.select_status(False)

        self.update_idletasks()

    def bindevents(self,onclick_callback):
        self._bind_all('<Button-1>',onclick_callback)

    def _bind_all(self,key,callback):
        for i in [self,self.innerframe,self.label,self.status,self.icon]:
            i.bind(key,callback)
    def select_status(self,selected):
        if selected:
            self._set_bg('#00A')
            self.label.config(fg='#FFF')
            self.status.config(fg='#DDD')
        else:
            self._set_bg('#FFF')
            self.label.config(fg='#000')
            self.status.config(fg='#AAA')
    def _set_bg(self,bgc):
        for i in [self,self.innerframe,self.label,self.status,self.icon]:
            i.config(bg=bgc)

class UserList(Canvas):
    _userlist = []
    _buttons  = []
    _icons    = {}
    _selected_index = -1

    def __init__(self, master, **options):
        self.base       = Canvas.__init__(self,master,**options)

        self._icons['online']  = './online.gif'
        self._icons['offline'] = './offline.gif'

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
    def _get_listitem(self,username,slogan,status,tag):
        if status == True:
            icon = self._icons['online']
        else:
            icon = self._icons['offline']
        btn = ListItem(self.frame)
        btn.itemize(username,slogan,icon,tag)
        return btn
    def add(self,username,slogan,status,tag=''):
        li = self._get_listitem(username,slogan,status,tag)
        li.pack(side=TOP,fill=X,expand=1)
        self._buttons.append(li)
        seqid = len(self._buttons)-1

        def _onclick(e,sid = seqid):
            self._selected_index = sid
            for i in range(0,len(self._buttons)):
                if i == sid:
                    self._buttons[i].select_status(True)
                else:
                    self._buttons[i].select_status(False)

        self._buttons[seqid].bindevents(_onclick)

        self._reset_scroll()
    def _reset_scroll(self):
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
    def _update_userlist(self):
        for btn  in self._buttons:
            self.tk.call('pack','forget',btn)
        self._buttons = []

        for item in self._userlist:
            self._buttons.append(btn)

        for btn  in self._buttons:
            btn.pack(side=TOP,fill=X,expand=1)

        self._reset_scroll()
            
if __name__ == '__main__':
    import time,random

    root = Tk()

    
    ul = UserList(root,bg='#F00')
    ul.grid(row=0,column=0)

    ul.add('You','Here is to display your status.',True)

    btn = Button(root,text='Add')
    def test():
        ul.add(str(time.time()),'当前在线',random.randint(0,1))
    btn['command'] = test
    btn.grid(row=1,column=0)
    """
    li = ListItem(root)
    li.itemize('From_HMX','This is his status.','./online.gif')
    li.grid(row=0,column=0)
    """

    root.mainloop()
