import threading
import random

def testRange():
  for i in range(10):
    print(str(i+1)+ " in " + threading.currentThread().getName()+ ". ")
def testSumList():
  sumList = []
  for i in range(5):
    sumList.append(random.randint(1,10))
  x = sum(sumList)
  print(str(x) + " in " + threading.currentThread().getName()+ ". ")

#running threads from functions without classes,
#use target instead of caling the funtion class(threading.Thread) and run(self) 
t1 = threading.Thread(name="Thread1", target= testRange)
t2 = threading.Thread(name="Thread2", target= testSumList)
t1.start()
t2.start()
