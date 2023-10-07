import sys
def generator(limit):
    i=0
    while i<= limit:
        yield i
        i +=1
        
gl=generator(1000000)
        
g=(i for i in range(100000))
l=[i for i in range(100000)]

print(sum(gl))
print(sys.getsizeof(gl))
print(sys.getsizeof(g))
print(sys.getsizeof(l))