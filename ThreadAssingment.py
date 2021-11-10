import time
import random
import math
import threading

class writeFile(threading.Thread):
  def run(self):
    f = open("text.txt", "w")
    f.write("Writing to this file")
    f.close()
    
class loopingTime(threading.Thread):
    def run(self):
      for i in range(10):
        print(str(i+1)+ " in " + threading.currentThread().getName())
        time.sleep(1)
class sumRandList(threading.Thread):
    def run(self):
        sumList = []
        for i in range(5):
          sumList.append(random.randint(1,10))
        x = sum(sumList)
        print(str(x) + " in " + threading.currentThread().getName())
        print("\n")
class sqrRandList(threading.Thread):
    def run(self):
        sqrList = []
        for i in range(5):
          sqrList.append(random.randint(1,10))
        x = sum(sqrList)
        y = math.sqrt(x)
        print(str(y) + " in " + threading.currentThread().getName())
        print("\n")

t1 = writeFile(name ="Thread1")
t2 = loopingTime(name = "Thread2")
t3 = sumRandList(name ="Thread3")
t4 = sqrRandList(name ="Thread4")
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()  
t2.join()
t3.join()
t4.join()
print("Threads end.")
