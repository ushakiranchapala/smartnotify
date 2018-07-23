import time
from threading import Thread

answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print "Too Slow"

Thread(target = check).start()

answer = raw_input("Input something: ")
