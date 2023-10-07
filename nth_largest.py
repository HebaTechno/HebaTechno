def nth_largest(lst,nth):
    sortedlist=sorted(lst)
    sortedlistdesc=sortedlist[::-1]
    return sortedlistdesc[nth-1]
 
lst=[7,19,2,3,6,1,22,54,0,4]    
print(nth_largest(lst,3))    