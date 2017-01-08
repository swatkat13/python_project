l=range(100)
sum=0
avg=[]
j=10
for i in l:
    if l.index(i) >= j:
        sum=sum+i
        avg.append((float(sum)/j))
        sum=sum-l[l.index(i)-j]
    else:
        sum=sum+i
        avg.append(0)

print l
print avg

