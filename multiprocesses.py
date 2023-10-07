from multiprocessing import process 
import os
def square_num():
    for i in range(100):
        i*i
c=os.cpu_count()
ps=[]
for p in range(c):
    p=process(target=square_num)
    ps.append(p)
    
for p in ps:
    p.start()
    
for p in ps:
    p.join()
    
print("end")           