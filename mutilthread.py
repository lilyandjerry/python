#!/usr/bin/python
# #coding:utf-8 
# filename：mutilthread.py

import threading
import time

class IEvent:
    def __init__(self):
        pass
    def on_event(self):
        raise AttributeError("sub-class must implementation")


class EventPrintLog(IEvent):
    content = None
    def __init__(self,iputcontent):
        IEvent.__init__(self)
        self.content = iputcontent
    def on_event(self):
        print "Event count is:",str(self.content)


class EventQueue:
    eventlist = None
    eventlock = None
    condit = None
    def __init__(self):
        self.eventlist = []
        self.eventlock = threading.Lock()
        self.condit = threading.Condition()
        pass

    def push_event(self,evt):
        self.eventlock.acquire()
        self.eventlist.insert(0,evt)
        self.eventlock.release()
        
        self.condit.acquire()
        self.condit.notify()
        self.condit.release()

    def pop_event(self):
        self.eventlock.acquire()
        evt =  self.eventlist.pop()
        self.eventlock.release()
        return evt

    def on_event(self):
        if len(self.eventlist) == 0:
            self.condit.acquire()
            self.condit.wait()
            self.condit.release()
        else:
            self.pop_event().on_event()
'''
class EventQuThread(threading.thread):
    eventq = None
    def __init__(self):
        threading.Thread.__init__(self)
        self.eventq = EventQueue()

    def run(self):
        self.eventq.on_event()
'''
    
class myThread (threading.Thread):   #继承父类threading.Thread
    eventq = None
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.eventq = EventQueue()
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print "Starting " + self.name
        var = 1
        while var == 1:
            self.eventq.on_event()
        print "Exiting " + self.name


def main(): 
    thread1  = myThread(1, "Thread-1", 1)
    thread1.start()

    var = 1
    tick = 0
    while var == 1:
        tick = tick + 1 
        eve = EventPrintLog("who are am"+str(tick))
        thread1.eventq.push_event(eve)
        time.sleep(1)

if __name__ == '__main__':  
    exited = False  
    main()  