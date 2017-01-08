l=range(100,0,-1)
sum=0
avg=[]
j=10
for i in l:
    #print l.index(i)
    if (l.index(i)+1)>=j:
        sum=sum+i
        avg.append(float(sum)/j)
        sum=sum-l[l.index(i)-j]
    else:
        sum=sum+i

print l
print avg

