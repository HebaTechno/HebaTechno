class User:
    def __init__(self,name,email,title,pswd):
        self.email = email 
        self.name=name
        self.title= title
        self.pswd=pswd
        
    def change_pasword(self,new_pswd):
        self.pswd=new_pswd
        
    def change_title(self,new_title):
        self.title=new_title  
        
    def print_user_info(self):
        print(f"{self.name} is a {self.title} you can contact him at {self.email}")   
        

user_one=User("Mohammed","Mahamed@gmail.com","Dr","xsa")   
user_one.print_user_info()
user_one.change_pasword("pass")
user_one.change_title("Vet")
user_one.print_user_info()