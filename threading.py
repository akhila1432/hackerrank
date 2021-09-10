from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        print("Hello")
        sleep(.2)
    
class Hi(Thread):
    def run(self):
        print("Hi")
        sleep(.2)
        
t1 = Hello()
t2 = Hi()

t1.start()
sleep(.2)
t2.start()