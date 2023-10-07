from threading import Thread , Lock
import time 
databaseValue=0
def increaseValue(lock):
    global databaseValue
    #lock.aquire()
    with lock:
        localValue=databaseValue
        localValue +=1
        time.sleep(0.1)
        databaseValue= localValue
   # lock.release()
if __name__=="__main__":    
  print("start",databaseValue)  
  lock=Lock() 
  thread1=Thread(target=increaseValue,args=(lock,))
  thread2=Thread(target=increaseValue,args=(lock,))
  thread1.start()
  thread1.join()
  thread2.start()
  thread2.join()

  print("end",databaseValue)    
    