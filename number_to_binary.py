def square_num(n):
    print(n%2,"  ",n)
    if(int(n/2)>0):
        square_num(int(n/2))
    
square_num(1024)