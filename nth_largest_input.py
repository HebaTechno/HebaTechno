def nth_largest(lst,nth):
    sortedlist=sorted(lst)
    sortedlistdesc=sortedlist[::-1]
    return sortedlistdesc[nth-1]
 
lst=[] 
n="" 
while n!="-1":
    n=input("please add number to your list. enter(-1) to end list\n")
    
    if int(n)>=0:
      lst.append(int(n))
print(lst)    
print(nth_largest(lst,3))    