import operator

l=range(100,1000)

l2=range(500,600)

f=operator.itemgetter(2,5,3)

print f(l)

print f(l2)

