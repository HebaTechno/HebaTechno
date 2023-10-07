class CallCount:
    def __init__(self,func):
        self.func=func
        self.calls=0
        
    def __call__(self,*args,**kwargs):
       self.calls +=1
       print(f"call no {self.calls}")
       return self.func(*args,**kwargs)
      
@CallCount
def sayhello():
     print("hello")   
         
sayhello()    
sayhello() 
sayhello()  
print("-----")
