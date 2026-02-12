import numpy as np
x=[3,5,2,9,7]
total=0
count=0
for i in x:
    total+=i
    count+=1
mean=total/count
print(mean)
x=np.array([3,5,2,9,7])
m=np.mean(x)
print(m)