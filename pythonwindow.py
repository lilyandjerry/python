#! /usr/bin/python

import Tkinter;
from Tkinter import * 

top = Tkinter.Tk();
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(top)          #  创建两个列表组件
listb2 = Listbox(top)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
top.mainloop();
print "Exit loop";