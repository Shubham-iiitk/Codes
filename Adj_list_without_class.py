# Adjlist without using class

from collections import defaultdict
m = defaultdict(list)
def adjlist(v1,v2):
    if v1!=v2:
       if v1 not in m:
         m[v1]=[v2]
       else:
          m[v1].append(v2)

adjlist(1,2)
adjlist(1,3)
adjlist(2,1)
adjlist(1,3)
adjlist(2,3)
print(m,'hfuas')


