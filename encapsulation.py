class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    @property
    def Name(self):
        return self.__name
        
    @Name.setter
    def Name(self,value):
       self.__name=value
    @property
    def Age(self):
        return self.__age
        
    @Age.setter
    def Age(self,value):
       self.__age=value   
       
         
p1=Person("mike",28)
print(p1.Name,p1.Age)   
p1.Name="Bob"
p1.Age=37
print(p1.Name,p1.Age)
      