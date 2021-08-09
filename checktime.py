import timeit

mylist=[12,16,90,5,34,21,345,678,23,43,215,89,0,312,45,654,32,22,123]

def f1():
    filter(43,mylist)

def f2():
    
    for i in mylist:
        if(i==43):
            pass
print(timeit.timeit(f1,number=1000000))
print(timeit.timeit(f2,number=1000000))