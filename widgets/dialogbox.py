# -*- coding: utf-8 -*-

# 显示聊天内容的对话框

from Tkinter import *
import hashlib

class DialogBox(Text):
    require_receipt = True

    def __init__(self,master,**options):
        Text.__init__(self,master,**options)
        self.config(padx=7,pady=5)

    def newrecord(self,headline,text,is_ours):
        tagbase = hashlib.md5(headline + text).hexdigest()
        if is_ours:
            fgc,bgc1 = '#00A','white'
            if self.require_receipt:
                bgc2 = '#FCC'
            else:
                bgc2 = 'white'
        else:
            fgc,bgc1,bgc2 = '#A00','white','white'
        self._append(tagbase + '/headline',headline + '\n',fgc,bgc1,0,10,'Sans 9 bold')
        self._append(tagbase + '/content' ,text + '\n','black',bgc2,15,10,'Sans 9')

        return tagbase

    def mark_received(self,tag):
        self.tag_config(tag + '/content',background='white')

    def _append(self,tag, content, fg_color, bg_color, lmargin, offset, font):
        self.config(state=NORMAL)
	self.tag_config(tag, foreground=fg_color, background=bg_color, lmargin1=lmargin,lmargin2=lmargin, offset=offset, font=font)
	self.insert(END,content,tag)
	self.yview(END)
	self.config(state=DISABLED) 

if __name__ == '__main__':
    root = Tk()
    box = DialogBox(root)
    box.pack(expand=1,fill=BOTH)
    #box.require_receipt = False
    box.newrecord('HMX (2012-12-21 05:30:29):','大叔……',False)
    receipt = box.newrecord('Whirlpool (2012-12-21 05:31:01):','哈' * 50 + '.' * 102,True)
#    box.mark_received(receipt)
    box.newrecord('HMX (2012-12-21 05:32:00):','= =......',False)
    root.mainloop()
