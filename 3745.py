# 3745 오름세
import bisect
try:
    while input():
        q=[]
        for i in map(int,input().split()):
            s=bisect.bisect_left(q,i)
            if s!=len(q):q[s]=i
            else:q+=[i]
        print(len(q))
except:exit()