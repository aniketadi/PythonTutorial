from functools import reduce;
f = lambda a, b : a+b
print(f(5,11))


#filter without lambda
num = [2,4,7,4,3,22,45,7,66,54,22]
def isEven(n):
    return n%2==0

evens = list(filter(isEven,num))
print(evens)



#filter using lambda
num = [2,4,7,4,3,22,45,7,66,54,22]
evens = list(filter(lambda n : n%2==0, num))
print(evens)


#Map function
doubles = list(map(lambda a: a*2, evens))
print(doubles)

#Reduce Function
totalCount = reduce(lambda a,b : a+b, doubles)
print(totalCount)