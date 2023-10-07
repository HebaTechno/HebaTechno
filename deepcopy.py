from copy import *
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Company:
    def __init__(self,boss,emp):
        self.boss=boss
        self.emp=emp
        
        
p1=Person('alex',26)
p2=Person('jhon',29)
company1=Company(p2,p1)
company2=deepcopy(company1)
company2.boss.age=32
print(company1.boss.age)  
print(company2.boss.age)    
          