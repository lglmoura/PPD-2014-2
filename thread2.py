#!/usr/bin/env python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, c, d):
        threading.Thread.__init__(self)
        self.count = c
        self.delay = d

    def run(self):
        print "Inicio thread " + self.getName()
        ct = 0
        while ct < self.count:
            time.sleep(self.delay)
            ct += 1
            print "%s: %s\n" % ( self.getName(), time.ctime(time.time()) )

mt = MyThread(3,2)
mt.start()

mt1 = MyThread(3,3)
mt1.start()


print 'fim'