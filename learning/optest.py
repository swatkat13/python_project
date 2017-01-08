import time
import operator

start_time = time.time()
'''i=10000
while i > 0:
    i-=1
'''
a= 100+100

print 'time taken = ' + str(time.time() - start_time)

start_time = time.time()
i=10000
while i > 0:
    i-=1
operator.add(100,100)

print 'time taken by operator = ' + str(time.time() - start_time)
