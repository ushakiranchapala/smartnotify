import multiprocessing
import time
import os
from pynput.keyboard import Key, Controller
keyboard = Controller()

# Your foo function
def foo(n):
    os.system('dlnast -l tmp.mp3')
    #for i in range(10000 * n):
     #   print "Tick"
      #  time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(10)
    #print ("q")
    keyboard.press('q')
    time.sleep(2)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()
