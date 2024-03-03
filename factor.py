import numpy as np
n = 317865430791171141162720477822970083373
#14466256053892976549

for i in range(1,1000,3):
    v=i*100000000
    a = np.arange(v,v+300000000)#2,708,000,000
    print(a)
    # print(n%14466256053892976549)
    print(n/a[a.size-1])
    a = n % a
    print(a)
    i = np.where(a==0)
    print(i)
    a=0
