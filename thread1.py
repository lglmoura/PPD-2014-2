#!/usr/bin/env python

import threading

class MyThread(threading.Thread):
    def run(self):
        print "Inicio thread " + self.getName()

mt = MyThread()
mt.start()

print 'fim'