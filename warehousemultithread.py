import time
from threading import Thread
import random

Orders = 0
totalorders = 0
Workers = 0
Shipping = 0

def func1():
    global Orders
    global totalorders
    while True:
        Orders = random.randrange(6)
        totalorders = totalorders + Orders
        for i in range(Orders):
            print("A customer ordered an Item")
            print(" ")
        time.sleep((random.randrange(5)))
        print("Total Items Ordered:", totalorders)
        print(" ")
    
def func2():
    global Workers
    global totalorders
    while True:
        print("Total Workers: ", Workers)
        if totalorders >= 1 and totalorders < 2:
            Workers = 1
            print("A worker has started working")
            time.sleep(3)
            totalorders -= 1
            print("A worker has shipped a package")
        elif totalorders >= 3 and totalorders < 6:
            Workers = 2
            print("A worker has started working")
            print("A worker has started working")
            time.sleep(2)
            totalorders -= 2
            print("A worker has shipped a package")
            print("A worker has shipped a package")
        elif totalorders > 6:
            Workers = 4
            print("A worker has started working")
            print("A worker has started working")
            print("A worker has started working")
            print("A worker has started working")
            time.sleep(1)
            totalorders -= 4
            print("A worker has shipped a package")
            print("A worker has shipped a package")
            print("A worker has shipped a package")
            print("A worker has shipped a package")
        else:
            time.sleep(1)
    


if True:
    Thread(target = func1).start()
    Thread(target = func2).start()
    
