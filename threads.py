from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)

class Hii(Thread):
    def run(self):
        for i in range(500):
            print("hii")
            sleep(1)

t1 = Hello()
t2 = Hii ()

t1.start()
sleep(0.2)
t2.start()