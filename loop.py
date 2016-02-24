#!/usr/bin/env python
import os, sys, tempfile
import time
import threading
from queue import Queue, Empty

BITRATE = 8 # 000
MINSAMPLE = BITRATE / 2

def receive(q):
    while True:
        q.put(sys.stdin.read())

def send(q):
    while True:
        try:
            next_sample_data
        except NameError:
            beginning = True
        else:
            beginning = False

        try:
            next_sample_data = q.get_nowait()
        except Empty:
            if beginning:
                continue
        else:
            if len(next_sample_data) < MINSAMPLE:
            #   sys.stderr.write('Sample is too small, skipping\n')
                continue
            if beginning:
                next_bar_time = time.time()

        if next_bar_time - MINSAMPLE < time.time():
            print(next_sample_data) # Write to dsp
            next_bar_time = next_bar_time + len(next_sample_data)
            
q = Queue()
threading.Thread(None, receive, args = (q,)).start()
threading.Thread(None, send, args = (q,)).start()
