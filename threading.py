from threading import Thread 
import time 
databaseValue=0
def increaseValue():
    global databaseValue
    localValue=databaseValue
    localValue +=1
    time.sleep(0.1)
    databaseValue= localValue
if __name__=="__main__":    
  print("start",databaseValue)  
 
  thread1=Thread(target=increaseValue)
  thread2=Thread(target=increaseValue)
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()

  print("end",databaseValue)    
    