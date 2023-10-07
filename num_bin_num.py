bins=[]
def square_num(n):
    print(n%2,"  ",n)
    bins.append(n%2)
    if(int(n/2)>0):
        square_num(int(n/2))
      
square_num(1024)
print("     0")
print("-------------")
print(bins)
print("-------------")

def bin_to_num(bin):
    bins=list(bin)
    num=0
    for i in range(len(bins)):
        num += 2**i*bins[i]
    print(num)  
    
bin_to_num(bins)      