# -*- coding: utf-8 -*-

# 显示聊天内容的对话框

from Tkinter import *

class DialogBox(Text):
    def __init__(self,master,**options):
        Text.__init__(self,master,**options)
        self.config(padx=7,pady=5)

    def newrec(self,headline,text):
        pass
    def _append(self,tag, content, fg_color='black', bg_color='white', lmargin=0):
        self.config(state=NORMAL)
	self.tag_config(tag, foreground=fg_color, background=bg_color, lmargin1=lmargin,lmargin2=lmargin)
	self.insert(END,content,tag)
	self.yview(END)
	self.config(state=DISABLED) 

if __name__ == '__main__':
    root = Tk()
    box = DialogBox(root)
    box.pack()
    box._append('tag1','This is some content\n','#A00','white',0)
    box._append('tag2','Yes' * 100 + '\n','#000','white',10)
    root.mainloop()
