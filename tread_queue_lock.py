from threading import Thread,Lock,current_thread
from queue import Queue

def worker(q,lock):
    while True:
      value=q.get()
      with lock:
        print(f"in {current_thread().name} got {value}")
      q.task_done()
if __name__=="__main__": 
    q=Queue()
    lock=Lock()
    for i in range(10):
      thread=Thread(target=worker,args=(q,lock))
      thread.daemon=True
      thread.start()
    
    for i in range(1,21):
      q.put(i)      

    q.join()
    print("end")    
    